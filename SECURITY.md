# Security

`ap1-run` is intended to be executed inside an institution's own perimeter,
against systems that institution operates, by that institution's own
personnel. This document states what it does, what it does not do, and how to
report a defect.

**Read this before running it against anything internal.** That is what it is
for.

---

## Network behaviour

**The instrument makes no network call except to the endpoint declared in
configuration.**

There is no telemetry, no analytics, no usage reporting, no licence check, no
update check, and no hosted component. Nothing is transmitted to ZORRZ
Financial Inc. or to any third party at any time.

The scoring pass makes no network call at all. It reads the transcript
produced by the execution pass and the sealed inputs, and writes a report.

**Verifying this.** The claim is testable rather than asserted: run the test
suite under a deny-all egress policy. It is offline by construction and passes
with no network access. For an execution run, a network monitor will show
traffic only to the configured endpoint.

---

## Credentials

**Credentials are never written to disk, to a command line, to a log, or to
the transcript.**

The API key for the worked example is read from an environment variable:

```bash
export AP1_SMOKE_API_KEY=<key>
```

On Windows the key may optionally be read from the Credential Manager instead.
No other credential is used, and the instrument requires no credential to run
its test suites.

**Error bodies are masked.** Provider error responses can echo credential
fragments — a rejected request may return part of the key in its message.
Before any error body is stored or raised, substrings matching credential
shapes are redacted. The endpoint, status code and error type are retained.

**What the instrument reports about a credential:** its length, and nothing
else.

---

## Code execution

The worked example includes a calculator tool. **It uses an AST evaluator with
an explicit allow-list of node types.**

There is no `eval`, no `exec` and no `compile` anywhere in the instrument or
in the example. The evaluator permits arithmetic operations over numeric
literals and rejects attribute access, imports, function calls, subscripting,
comprehensions and name resolution. Its self-test asserts that each of these
is refused.

**This matters because the expression being evaluated originates from the
system under test.** A model that emits a malicious expression must not be
able to execute anything.

**If you supply your own tool implementation,** it runs with whatever
privileges you give it. The instrument does not sandbox operator-supplied
tools and does not claim to. That is your boundary to establish.

---

## Data handling

**No data leaves your perimeter.**

The fixture, the question set, the ground-truth module and the resulting
transcripts are files on your filesystem. The instrument reads them and writes
its output alongside them.

**Transcripts contain the full text of every request and response**, including
whatever your fixture contains and whatever the system under test returned.
Treat the output directory with the same controls you would apply to the
source data. It is gitignored by default so that run artifacts are not
committed accidentally.

**Use synthetic fixtures.** The instrument is designed to run against
representative data, not production records. Nothing enforces this and nothing
can.

---

## Dependencies

**One external dependency: `requests`.** Everything else is Python standard
library.

This is deliberate. An instrument an institution is asked to run inside its
perimeter should be readable by the security function reviewing it, and a
dependency tree is the part that cannot be read.

There is no package manager configuration that pulls transitive dependencies
at install time beyond `requests` and its own.

---

## Integrity

**The standard text is sealed.** `reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md` is
hashed into the pre-registration record before any request is sent, and a run
declaring a hash that does not match the file is refused.

`.gitattributes` marks `reference/` as not text, so the file passes through git
unmodified on every platform and its hash remains byte-identical to the
deposited version. Verify it against the DOI:

```bash
sha256sum reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md
# 48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56
```

**Every input is sealed before execution.** Fixture, question set, ground-truth
module and resolved configuration are hashed and timestamped, and the record’s
hash appears on every transcript line. A transcript cannot be silently paired
with a different fixture.

---

## What this instrument does not protect against

Stated because an incomplete list is worse than none.

- **It does not sandbox operator-supplied tools.** Your tool implementations
  run with the privileges you grant them.
- **It does not validate your fixture.** A fixture containing real customer
  data will be processed as readily as a synthetic one.
- **It does not protect the endpoint under test.** Adversarial items in your
  question set are sent to your system as written.
- **It is not a security assessment.** It measures numerical admissibility.
  A system can score well on every dimension and be insecure.

---

## Reporting a vulnerability

Report to **mrupp@zorrz.com**.

Please include what you found, how to reproduce it, and what you think the
impact is. If the finding concerns credential handling, network behaviour or
code execution, say so in the subject line.

**Findings will be published.** A defect in an instrument that measures
provenance is a defect worth others knowing about, and correction is by
addition — the record is not edited to look clean.

---

*ZORRZ Financial Inc. · Last reviewed 7 August 2026*
