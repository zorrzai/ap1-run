"""R0.4 -- Numeric, Parsing and Hashing Discipline.

Spec: AP-1 Runner Build Spec v0.3, section 3 R0.4.
Classification: DETERMINISTIC.

All numeric values on comparison paths are Decimal, parsed from string.
Binary floating-point arithmetic is prohibited anywhere a value is
compared, quantised, or reported.
"""

from decimal import (Context, Decimal, DivisionByZero, InvalidOperation,
                     Overflow, ROUND_HALF_UP, ROUND_HALF_EVEN, localcontext)
import hashlib
import json
import re
from typing import NamedTuple


# -- Exceptions ------------------------------------------------------

class AmbiguousLocaleError(Exception):
    """Token admits more than one reading under configured separators."""


class NumericParseError(Exception):
    """String cannot be parsed as a numeric value per R0.4.2."""


# -- R0.4.2 Parsed token ---------------------------------------------

class NumericToken(NamedTuple):
    """A parsed numeric value with metadata per R0.4.2 grammar."""
    value: Decimal
    percent: bool
    currency: str       # empty string if none
    literal: str        # original text as matched
    start: int          # offset in source text
    end: int


# -- R0.4.2 Single-value parsing -------------------------------------

def parse_decimal(text, *, decimal_sep='.', grouping_sep=',',
                  currency_symbols=None):
    """Parse a single numeric string per R0.4.2 grammar.

    Returns (value: Decimal, is_percent: bool, currency: str).
    Parses to Decimal from literal text -- NEVER through float.

    Percentages: '12.5%' -> (Decimal('12.5'), True, '').
    Parenthesised negatives: '(1,780.00)' -> (Decimal('-1780.00'), False, '').
    """
    if currency_symbols is None:
        currency_symbols = []

    s = text.strip()
    if not s:
        raise NumericParseError('empty string')

    is_neg = False
    is_pct = False
    cur = ''

    # Step 1: parenthesised negative
    if s.startswith('(') and s.endswith(')'):
        is_neg = True
        s = s[1:-1].strip()

    # Step 2: leading currency (longest match first)
    for sym in sorted(currency_symbols, key=len, reverse=True):
        if s.startswith(sym):
            cur = sym
            s = s[len(sym):].strip()
            break

    # Step 3: sign (if not already from parens). One sign at most: a
    # second one, or a sign inside parentheses, is left in the digit
    # string and refused by the grammar check (step 11).
    if not is_neg and s and s[0] in '+-\u2212':
        is_neg = s[0] in '-\u2212'
        s = s[1:].strip()

    # Step 3b: leading currency after sign (handles -$2411.00)
    if not cur:
        for sym in sorted(currency_symbols, key=len, reverse=True):
            if s.startswith(sym):
                cur = sym
                s = s[len(sym):].strip()
                break

    # Step 4: trailing percent
    if s.endswith('%'):
        is_pct = True
        s = s[:-1].strip()

    # Step 5: trailing currency (if none found leading)
    if not cur:
        for sym in sorted(currency_symbols, key=len, reverse=True):
            if s.endswith(sym):
                cur = sym
                s = s[:-len(sym)].strip()
                break

    # Step 5b: a percent before a trailing currency ('5%$', '10%USD')
    if not is_pct and cur and s.endswith('%'):
        is_pct = True
        s = s[:-1].strip()

    # Step 6: something must be left (the grammar is checked in step 11)
    if not s:
        raise NumericParseError(f'no digits in: {text!r}')

    # Step 7: ambiguity check
    _check_ambiguity(s, decimal_sep, grouping_sep)

    digits = s

    # Step 8: remove grouping separators
    if grouping_sep and grouping_sep != decimal_sep:
        s = s.replace(grouping_sep, '')

    # Step 9: normalise decimal separator to '.'
    if decimal_sep != '.':
        s = s.replace(decimal_sep, '.', 1)

    # Step 10: parse to Decimal -- NEVER through float
    try:
        value = Decimal(s)
    except InvalidOperation:
        raise NumericParseError(
            f'cannot parse as Decimal: {s!r} from {text!r}')

    # Step 11: the digit string must be in the R0.4.2 grammar: digits,
    # optionally grouped in threes by the grouping separator, with an
    # optional decimal part. Decimal() alone also accepts NaN, Infinity,
    # exponents, underscores and a second sign, and step 8 removes a
    # grouping separator wherever it is.
    if not _digit_grammar(decimal_sep, grouping_sep).fullmatch(digits):
        raise NumericParseError(
            f'not a number under R0.4.2: {digits!r} from {text!r}')

    if is_neg:
        value = -value

    return value, is_pct, cur


def _digit_grammar(decimal_sep, grouping_sep):
    """Regex for the unsigned digit string of R0.4.2.

    Integer part: digits, or groups of three after a leading group of
    one to three when a grouping separator is configured. Then an
    optional decimal separator and digits. At least one digit.
    """
    d = re.escape(decimal_sep)
    if grouping_sep and grouping_sep != decimal_sep:
        g = re.escape(grouping_sep)
        integer = r'(?:\d{1,3}(?:' + g + r'\d{3})+|\d+)'
    else:
        integer = r'\d+'
    return re.compile(
        '(?:' + integer + '(?:' + d + r'\d*)?' + '|' + d + r'\d+)')


def _check_ambiguity(digit_str, decimal_sep, grouping_sep):
    """Raise AmbiguousLocaleError when separators cannot disambiguate.

    Ambiguity arises when decimal_sep == grouping_sep and the
    separator appears in the text.
    """
    if decimal_sep == grouping_sep and decimal_sep in digit_str:
        raise AmbiguousLocaleError(
            f'{digit_str!r}: separator {decimal_sep!r} is configured '
            f'as both decimal and grouping -- cannot disambiguate')


# -- R0.4.2 Extraction from free text --------------------------------

def _build_extraction_re(decimal_sep, grouping_sep, currency_symbols):
    """Build a compiled regex to find numeric token candidates."""
    d = re.escape(decimal_sep)
    g = re.escape(grouping_sep) if grouping_sep else None

    # Integer with optional grouping
    if g:
        num_int = r'\d{1,3}(?:' + g + r'\d{3})+'
        num_any = '(?:' + num_int + r'|\d+)'
    else:
        num_any = r'\d+'

    # Optional fractional part
    num_frac = '(?:' + d + r'\d+)?'
    num = num_any + num_frac

    # Currency alternation (optional)
    if currency_symbols:
        syms = sorted(currency_symbols, key=len, reverse=True)
        cur = '(?:' + '|'.join(re.escape(s) for s in syms) + ')'
        cur_lead = '(?:' + cur + r'\s*)?'
        cur_trail = r'(?:\s*' + cur + ')?'
    else:
        cur_lead = ''
        cur_trail = ''

    pats = []

    # 1: Parenthesised: ( [cur] num [%] [cur] )
    pats.append(r'\(\s*' + cur_lead + num + r'\s*%?' + cur_trail + r'\s*\)')

    # 2: Currency-led: cur [sign] num [%]
    if currency_symbols:
        pats.append(cur + r'\s*[+\-\u2212]?\s*' + num + r'\s*%?')

    # 3: Sign-led: sign [cur] num [%] [cur]
    pats.append(r'[+\-\u2212]\s*' + cur_lead + num + r'\s*%?' + cur_trail)

    # 4: Bare: num [%] [cur]
    pats.append(num + r'\s*%?' + cur_trail)

    return re.compile('|'.join(pats))


_SIGNS = '+-\u2212'
_WORD_CHAR = re.compile(r'\w')


def extract_numeric_tokens(text, *, decimal_sep='.', grouping_sep=',',
                           currency_symbols=None):
    """Extract all numeric tokens from free text per R0.4.2.

    Returns list of NumericToken sorted by position.
    Raises AmbiguousLocaleError if any token is ambiguous.

    Two readings of the free text, beyond the token grammar:
    - A sign directly after a number (only whitespace between) is a
      binary operator, not the sign of the next token: '1437.00 - 1006.25'
      and '5-3' give 1006.25 and 3 (S3-G1-5).
    - Digits inside a word are not a token: 'Q04', 'v2.0.1', 'item A1'
      give nothing (S3-G1-6). A match is inside a word when a word
      character touches its first or last character (both word
      characters), or when it is joined to such a match by separator
      characters only, or by nothing ('v2.0.1': '2.0' and '1'; 'Q4-5').
    """
    if currency_symbols is None:
        currency_symbols = []

    pat = _build_extraction_re(decimal_sep, grouping_sep, currency_symbols)

    raw = []
    for m in pat.finditer(text):
        raw.append((m.start(), m.end(), m.group()))

    # Deduplicate overlapping spans -- keep longest
    raw.sort(key=lambda x: (x[0], -(x[1] - x[0])))
    deduped = []
    last_end = -1
    for start, end, txt in raw:
        if start >= last_end:
            deduped.append((start, end, txt))
            last_end = end

    in_word = _matches_inside_words(text, deduped, decimal_sep, grouping_sep)

    tokens = []
    prev_core_end = None
    for i, (start, end, match_text) in enumerate(deduped):
        core_end = start + len(match_text.rstrip())
        follows_number = (prev_core_end is not None
                          and not text[prev_core_end:start].strip())
        prev_core_end = core_end
        if in_word[i]:
            continue
        stripped = match_text.strip()
        if follows_number and stripped[0] in _SIGNS:
            # An operator: the token is what follows it.
            rest = stripped[1:].lstrip()
            start = core_end - len(rest)
            stripped = rest
        if not stripped or not any(c.isdigit() for c in stripped):
            continue
        try:
            value, is_pct, cur = parse_decimal(
                stripped,
                decimal_sep=decimal_sep,
                grouping_sep=grouping_sep,
                currency_symbols=currency_symbols)
        except NumericParseError:
            continue
        # AmbiguousLocaleError propagates to caller

        tokens.append(NumericToken(
            value=value, percent=is_pct, currency=cur,
            literal=stripped, start=start, end=end))

    return tokens


def _matches_inside_words(text, matches, decimal_sep, grouping_sep):
    """For each match, whether it is part of a word (see
    extract_numeric_tokens). Consecutive matches with nothing but
    separator characters between them are joined; a match touching a
    word character puts every match joined to it inside the word."""
    seps = {c for c in (decimal_sep, grouping_sep) if c and not c.isspace()}
    spans = [(start, start + len(match_text.rstrip()))
             for start, _end, match_text in matches]

    def touches_word(start, core_end):
        return bool((start > 0 and _WORD_CHAR.match(text[start - 1])
                     and _WORD_CHAR.match(text[start]))
                    or (core_end < len(text)
                        and _WORD_CHAR.match(text[core_end])
                        and _WORD_CHAR.match(text[core_end - 1])))

    in_word = [touches_word(start, core_end) for start, core_end in spans]
    # joined[i]: match i and match i + 1 are one run
    joined = [set(text[spans[i][1]:spans[i + 1][0]]) <= seps
              for i in range(len(spans) - 1)]
    for i, link in enumerate(joined):
        if link and in_word[i]:
            in_word[i + 1] = True
    for i, link in reversed(list(enumerate(joined))):
        if link and in_word[i + 1]:
            in_word[i] = True
    return in_word


# -- R0.4.1 Decimal context -------------------------------------------

# The one Decimal context for arithmetic on comparison paths (T3-60).
# Modules use it locally (`with localcontext(DECIMAL_CONTEXT):`) and
# never change the global context, so a result does not depend on which
# modules happen to have been imported. Precision 50 is what the live
# runner used before (invocation.py set it globally on import).
DECIMAL_CONTEXT = Context(
    prec=50, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
    capitals=1, clamp=0, flags=[],
    traps=[InvalidOperation, DivisionByZero, Overflow])


# -- R0.4.1 Quantisation ---------------------------------------------

ROUNDING_MODES = {
    'ROUND_HALF_UP': ROUND_HALF_UP,
    'ROUND_HALF_EVEN': ROUND_HALF_EVEN,
}


def quantise(value, places, rounding='ROUND_HALF_UP'):
    """Quantise a Decimal to the given number of decimal places.

    Applied ONCE, at the declared point. Intermediates are carried
    at full precision. Runs in DECIMAL_CONTEXT, whatever the caller's
    context. `places` is a non-negative int.
    """
    mode = ROUNDING_MODES.get(rounding)
    if mode is None:
        raise ValueError(f'unsupported rounding mode: {rounding!r}')
    if (not isinstance(places, int) or isinstance(places, bool)
            or places < 0):
        raise ValueError(
            f'quantisation places must be a non-negative int: {places!r}')
    with localcontext(DECIMAL_CONTEXT):
        q = Decimal(10) ** -places
        return value.quantize(q, rounding=mode)


# -- R0.4.3 Canonical hashing ----------------------------------------

def _check_no_float(obj, path='$'):
    """Refuse any float in the data structure, as a value or as a dict
    key (T3-71). R0.4.1 enforcement."""
    if isinstance(obj, float):
        raise TypeError(
            f'float at {path}: {obj!r} -- R0.4.1 prohibits float '
            f'on comparison paths')
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, float):
                raise TypeError(
                    f'float key at {path}: {k!r} -- R0.4.1 prohibits '
                    f'float on comparison paths')
            _check_no_float(v, f'{path}.{k}')
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            _check_no_float(v, f'{path}[{i}]')


class _DecimalEncoder(json.JSONEncoder):
    """JSON encoder serialising Decimals as exact string representation."""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

def canonical_json(obj):
    """Canonical JSON: sorted keys, no whitespace, Decimals as strings.

    R0.4.3: UTF-8 JSON with sorted keys, no insignificant whitespace,
    Decimal values serialised as their exact string representation.
    Timestamps ISO-8601 UTC.
    """
    _check_no_float(obj)
    return json.dumps(obj, cls=_DecimalEncoder, sort_keys=True,
                      separators=(',', ':'), ensure_ascii=False)

def canonical_hash(obj):
    """SHA-256 hex digest of the canonical JSON of obj. R0.4.3."""
    text = canonical_json(obj)
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def file_hash(path):
    """SHA-256 hex digest of a file's raw bytes."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()
