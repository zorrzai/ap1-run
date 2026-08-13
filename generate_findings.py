#!/usr/bin/env python3
"""
generate_findings.py — Generate FINDINGS.md from run artifacts and template.

Reads smoke_summary.json for both runs, computes every artifact-derived
figure using Decimal arithmetic, substitutes into FINDINGS.template.md,
and writes FINDINGS.md.

A placeholder with no computed value is a FATAL error.
A computed value with no placeholder is reported as UNUSED on stderr.

Part of the AP-1 runner build pipeline.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal, getcontext, ROUND_HALF_UP
from report import clopper_pearson_upper_k0

getcontext().prec = 50

ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(ROOT, "output")
TEMPLATE = os.path.join(ROOT, "FINDINGS.template.md")
TARGET = os.path.join(ROOT, "FINDINGS.md")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def pct(num, denom, places=1):
    """Compute percentage using Decimal, quantised to `places` decimal places."""
    if denom == 0:
        return Decimal("0")
    q = Decimal("0.1") if places == 1 else Decimal(10) ** -places
    return (Decimal(num) / Decimal(denom) * 100).quantize(q)


def fmt(n):
    """Format integer with comma separators."""
    if isinstance(n, Decimal):
        # For decimal results, return as-is
        return str(n)
    return f"{n:,}"


def classify_originated_mechanism(provenance_result):
    """Classify an OPERAND-ORIGINATED provenance outcome by mechanism.

    Returns one of: 'sign_inv', 'ungrounded', 'untraceable'.
    Precondition: provenance_result['outcome'] == 'OPERAND-ORIGINATED'.
    """
    has_cis = any(
        res.get("resolution") == "computed_in_session_ungrounded"
        for res in provenance_result.get("operand_resolutions", [])
    )
    has_sign = any(
        res.get("sign_inversion_finding") not in (None, False)
        for res in provenance_result.get("operand_resolutions", [])
    )
    if has_cis:
        return "ungrounded"
    elif has_sign:
        return "sign_inv"
    else:
        return "untraceable"


def compute_figures():
    """Compute every placeholder value from the run artifacts."""
    run_a = load_json(os.path.join(OUTPUT, "run_a_mini", "smoke_summary.json"))
    run_b = load_json(os.path.join(OUTPUT, "run_b_sol", "smoke_summary.json"))
    run_s = load_json(os.path.join(
        OUTPUT, "superseded", "run_b_sol_pre_restructure", "smoke_summary.json"))

    v = {}  # All placeholder values

    def run_core(results, pfx):
        """Extract core metrics for one run."""
        total = len(results)
        base = [r for r in results if r["condition"] == "base"]
        ir = [r for r in results if r["condition"] == "instruction_removed"]

        v[f"{pfx}_total_entries"] = total
        v[f"{pfx}_base_count"] = len(base)
        v[f"{pfx}_ir_count"] = len(ir)

        # Invocation
        v[f"{pfx}_invoked_base"] = sum(1 for r in base if r["invocation_outcome"] == "INVOKED")
        v[f"{pfx}_not_invoked_ir"] = sum(1 for r in ir if r["invocation_outcome"] == "NOT-INVOKED")
        v[f"{pfx}_invoked_ir"] = sum(1 for r in ir if r["invocation_outcome"] == "INVOKED")

        # NOT-INVOKED by item
        ni_items = Counter(r["item_id"] for r in ir if r["invocation_outcome"] == "NOT-INVOKED")
        for item, count in ni_items.items():
            v[f"{pfx}_ni_{item}"] = count

        # Operation correctness
        total_ops = 0
        wrong_ops = 0
        correct_ops = 0
        op_by_cond = defaultdict(lambda: {"wo": 0, "oc": 0, "total": 0})
        op_by_item = defaultdict(lambda: {"wo": 0, "total": 0})
        for r in results:
            for op in r.get("operation_correctness", []):
                total_ops += 1
                op_by_cond[r["condition"]]["total"] += 1
                op_by_item[r["item_id"]]["total"] += 1
                if op["outcome"] == "WRONG-OPERATION":
                    wrong_ops += 1
                    op_by_cond[r["condition"]]["wo"] += 1
                    op_by_item[r["item_id"]]["wo"] += 1
                else:
                    correct_ops += 1
                    op_by_cond[r["condition"]]["oc"] += 1

        v[f"{pfx}_total_ops"] = total_ops
        v[f"{pfx}_wrong_ops"] = wrong_ops
        v[f"{pfx}_correct_ops"] = correct_ops
        v[f"{pfx}_wo_pct"] = pct(wrong_ops, total_ops)
        v[f"{pfx}_wo_base"] = op_by_cond["base"]["wo"]
        v[f"{pfx}_total_base_ops"] = op_by_cond["base"]["total"]
        v[f"{pfx}_wo_base_pct"] = pct(op_by_cond["base"]["wo"], op_by_cond["base"]["total"])
        v[f"{pfx}_wo_ir"] = op_by_cond["instruction_removed"]["wo"]
        v[f"{pfx}_total_ir_ops"] = op_by_cond["instruction_removed"]["total"]
        v[f"{pfx}_wo_ir_pct"] = pct(
            op_by_cond["instruction_removed"]["wo"],
            op_by_cond["instruction_removed"]["total"],
        )
        v[f"{pfx}_ni_pct"] = pct(v[f"{pfx}_not_invoked_ir"], len(ir))

        # WRONG-OP split
        wo_correct = wo_wrong = wo_adj = 0
        for r in results:
            for op in r.get("operation_correctness", []):
                if op["outcome"] == "WRONG-OPERATION":
                    fig = r["figure_outcome"]
                    if fig == "AUTO-MATCH":
                        wo_correct += 1
                    elif fig in ("AUTO-MISMATCH", "MISMATCH"):
                        wo_wrong += 1
                    else:
                        wo_adj += 1
        v[f"{pfx}_wo_route_divergence"] = wo_correct
        v[f"{pfx}_wo_item_wrong"] = wo_wrong
        v[f"{pfx}_wo_adjudicated"] = wo_adj

        # Provenance
        prov_g = prov_o = total_prov = 0
        for r in results:
            for p in r.get("provenance_results", []):
                total_prov += 1
                if p["outcome"] == "OPERANDS-GROUNDED":
                    prov_g += 1
                elif p["outcome"] == "OPERAND-ORIGINATED":
                    prov_o += 1
        v[f"{pfx}_prov_grounded"] = prov_g
        v[f"{pfx}_prov_originated"] = prov_o
        v[f"{pfx}_total_prov"] = total_prov
        v[f"{pfx}_grounded_pct"] = pct(prov_g, total_prov)
        v[f"{pfx}_originated_pct"] = pct(prov_o, total_prov)

        # Operand resolutions
        res_counter = Counter()
        total_res = 0
        for r in results:
            for p in r.get("provenance_results", []):
                for res in p.get("operand_resolutions", []):
                    total_res += 1
                    res_counter[res.get("resolution", "UNKNOWN")] += 1
        v[f"{pfx}_total_resolutions"] = total_res
        for res_type in ["source_match", "constant", "transformed_source",
                         "intermediate", "computed_in_session",
                         "computed_in_session_ungrounded", "originated"]:
            v[f"{pfx}_res_{res_type}"] = res_counter.get(res_type, 0)
        # Alias for template short name
        v[f"{pfx}_res_cis_ungrounded"] = res_counter.get("computed_in_session_ungrounded", 0)

        # Sign inversions (operand_resolutions with sign_inversion_finding)
        sign_inv = 0
        for r in results:
            for p in r.get("provenance_results", []):
                for res in p.get("operand_resolutions", []):
                    sif = res.get("sign_inversion_finding")
                    if sif is not None and sif is not False:
                        sign_inv += 1
        v[f"{pfx}_sign_inversions"] = sign_inv

        # Originated operands — values
        orig_vals = Counter()
        for r in results:
            for p in r.get("provenance_results", []):
                for orig in p.get("originated_operands", []):
                    val = str(orig.get("value", orig) if isinstance(orig, dict) else orig)
                    orig_vals[val] += 1
        v[f"{pfx}_total_originated_operands"] = sum(orig_vals.values())
        # Store individual originated values and their counts
        v[f"{pfx}_orig_vals"] = dict(orig_vals)

        # Originated operand values that are sign-inversions by value
        sign_inv_operand_vals = sum(
            c for val, c in orig_vals.items() if val in ("-12.0", "-12")
        )
        v[f"{pfx}_sign_inv_operand_vals"] = sign_inv_operand_vals

        # Outcome-level breakdown: classify each OPERAND-ORIGINATED outcome
        outcomes = Counter()
        item_mechanism = defaultdict(Counter)  # {item_id: {mechanism: count}}
        for r in results:
            item_id = r["item_id"]
            for p in r.get("provenance_results", []):
                if p["outcome"] != "OPERAND-ORIGINATED":
                    continue
                mech = classify_originated_mechanism(p)
                outcomes[mech] += 1
                item_mechanism[item_id][mech] += 1

        v[f"{pfx}_outcomes_sign_inv"] = outcomes["sign_inv"]
        v[f"{pfx}_outcomes_ungrounded"] = outcomes["ungrounded"]
        v[f"{pfx}_outcomes_untraceable"] = outcomes["untraceable"]

        # Originated by item (total and per-mechanism)
        for item_id in sorted(item_mechanism):
            mechs = item_mechanism[item_id]
            total = sum(mechs.values())
            v[f"{pfx}_orig_item_{item_id}"] = total
            for mech_name, count in mechs.items():
                v[f"{pfx}_orig_item_{item_id}_{mech_name}"] = count

        # D1
        d1 = Counter(r["figure_outcome"] for r in results)
        v[f"{pfx}_d1_auto_match"] = d1.get("AUTO-MATCH", 0)

        # Per-item detail
        for qid in ["Q07", "Q08", "Q10"]:
            qr = [r for r in results if r["item_id"] == qid]
            qd1 = Counter(r["figure_outcome"] for r in qr)
            qwo = sum(1 for r in qr for op in r.get("operation_correctness", [])
                       if op["outcome"] == "WRONG-OPERATION")
            qtot = sum(1 for r in qr for op in r.get("operation_correctness", []))
            v[f"{pfx}_{qid}_auto_match"] = qd1.get("AUTO-MATCH", 0)
            v[f"{pfx}_{qid}_total"] = len(qr)
            v[f"{pfx}_{qid}_wo"] = qwo
            v[f"{pfx}_{qid}_total_ops"] = qtot
            if qtot > 0:
                v[f"{pfx}_{qid}_wo_pct"] = pct(qwo, qtot)

        # Q08 base only
        q08_base = [r for r in base if r["item_id"] == "Q08"]
        v[f"{pfx}_Q08_base_am"] = sum(1 for r in q08_base if r["figure_outcome"] == "AUTO-MATCH")
        v[f"{pfx}_Q08_base_total"] = len(q08_base)

        # Step-4 by item
        step4_by_item = defaultdict(int)
        for r in results:
            for p in r.get("provenance_results", []):
                for res in p.get("operand_resolutions", []):
                    if res.get("resolution") == "computed_in_session":
                        step4_by_item[r["item_id"]] += 1
        v[f"{pfx}_step4_total"] = sum(step4_by_item.values())
        for item, count in step4_by_item.items():
            v[f"{pfx}_step4_{item}"] = count

    run_core(run_a["all_results"], "a")
    run_core(run_b["all_results"], "b")

    # Originated operand values — distinct sets for template
    for pfx, results in [("a", run_a["all_results"]), ("b", run_b["all_results"])]:
        orig = v[f"{pfx}_orig_vals"]
        for val_name, val_key in [
            ("1.0065", "1.0065"), ("45", "45"), ("2", "2"),
            ("1.18", "1.18"), ("1.015", "1.015"), ("35.63", "35.63"),
            ("2436", "2436"), ("-12.0", "-12.0"), ("-12", "-12"),
            ("233.54166666666666", "233.54166666666666"),
        ]:
            v[f"{pfx}_orig_{val_key}"] = orig.get(val_key, 0)

    # Derived counts
    v["b_untraceable"] = (
        v["b_total_originated_operands"]
        - v.get("b_orig_2", 0)
        - v.get("b_orig_45", 0)  # wait, 45 IS untraceable
    )
    # Actually: b_untraceable = b_total_originated - b_orig_2
    # because 2 is the declared constant, rest are untraceable
    v["b_untraceable"] = v["b_total_originated_operands"] - v.get("b_orig_2", 0)
    v["b_orig_2_count"] = v.get("b_orig_2", 0)
    v["b_orig_1_0065_count"] = v.get("b_orig_1.0065", 0)
    v["b_orig_45_count"] = v.get("b_orig_45", 0)

    v["a_untraceable"] = v["a_outcomes_untraceable"]
    v["a_ungrounded_chain"] = v["a_outcomes_ungrounded"]

    # Q07 recomputation
    balance = Decimal("42175.00")
    rate = Decimal("7.8")
    fee = Decimal("15.00")
    monthly_rate = rate / 100 / 12
    factor = 1 + monthly_rate
    simple = (balance * monthly_rate - fee) * 3
    compound = balance * (factor ** 3 - 1) - fee * 3
    v["q07_simple"] = simple.quantize(Decimal("0.01"))
    v["q07_compound"] = compound.quantize(Decimal("0.01"))
    v["q07_difference"] = (compound - simple).quantize(Decimal("0.01"))

    # Combined untraceable
    v["combined_untraceable"] = v["a_untraceable"] + v["b_untraceable"]

    # Derived percentages for template (replacing hardcoded literals)
    for pfx in ("a", "b"):
        for qid in ("Q07", "Q08", "Q10"):
            total_key = f"{pfx}_{qid}_total"
            am_key = f"{pfx}_{qid}_auto_match"
            if total_key in v and am_key in v and v[total_key] > 0:
                v[f"{pfx}_{qid}_am_pct"] = pct(v[am_key], v[total_key])

    # Ops per execution (for F4)
    v["b_ops_per_exec"] = round(v["b_total_ops"] / v["b_total_entries"], 2)

    # Q10 calls per execution for Run A
    q10_a = [r for r in run_a["all_results"] if r["item_id"] == "Q10"]
    q10_ops = sum(len(r.get("operation_correctness", [])) for r in q10_a)
    q10_count = len(q10_a) if len(q10_a) > 0 else 1
    v["a_Q10_calls_per_exec"] = round(q10_ops / q10_count, 1)

    # F8 base non-invocations
    for pfx, run in [("a", run_a), ("b", run_b)]:
        base_r = [r for r in run["all_results"] if r["condition"] == "base"]
        v[f"{pfx}_not_invoked_base"] = sum(
            1 for r in base_r if r["invocation_outcome"] == "NOT-INVOKED")

    # D7.5 Clopper-Pearson bounds for zero-failure figures
    # The zero item-wrong count holds over the AUTO-SCORED population only.
    # Adjudicated cases are undetermined and cannot support the zero.
    for pfx, results in [("a", run_a["all_results"]), ("b", run_b["all_results"])]:
        auto_scored_wo = 0
        auto_scored_wrong = 0
        for r in results:
            fig = r.get("figure_outcome", "")
            is_auto = fig.startswith("AUTO-")
            for op in r.get("operation_correctness", []):
                if op["outcome"] == "WRONG-OPERATION" and is_auto:
                    auto_scored_wo += 1
                    if fig == "AUTO-MISMATCH":
                        auto_scored_wrong += 1
        v[f"{pfx}_wo_auto_scored"] = auto_scored_wo
        v[f"{pfx}_wo_auto_wrong"] = auto_scored_wrong
        if auto_scored_wrong == 0 and auto_scored_wo > 0:
            bound = clopper_pearson_upper_k0(auto_scored_wo)
            v[f"{pfx}_wo_item_wrong_cp"] = (
                f"0/{auto_scored_wo:,} auto-scored "
                f"(p_upper < {bound:.4f}, 95% Clopper–Pearson)")
        else:
            v[f"{pfx}_wo_item_wrong_cp"] = f"{auto_scored_wrong}/{auto_scored_wo:,}"

    # D7.5 bound for zero base non-invocations (D7.1b invocation figure)
    for pfx in ("a", "b"):
        k_val = v.get(f"{pfx}_not_invoked_base", 0)
        n_val = 500  # 10 items x 50 repeats, base condition
        if k_val == 0 and n_val > 0:
            bound = clopper_pearson_upper_k0(n_val)
            v[f"{pfx}_base_noninvoke_cp"] = (
                f"0/{n_val} "
                f"(p_upper < {bound:.4f}, 95% Clopper–Pearson)")
        else:
            v[f"{pfx}_base_noninvoke_cp"] = f"{k_val}/{n_val}"


    # F2 superseded
    sup_results = run_s["all_results"]
    sup_orig_vals = Counter()
    for r in sup_results:
        for p in r.get("provenance_results", []):
            for orig in p.get("originated_operands", []):
                val_str = str(orig.get("value", orig) if isinstance(orig, dict) else orig)
                sup_orig_vals[val_str] += 1
    sup_total = sum(sup_orig_vals.values())
    sup_const_1 = sup_orig_vals.get("1", 0)
    sup_remaining = sup_total - sup_const_1
    sup_sign_conv_keys = ["2400", "2400.0", "2400.00", "287500", "287500.0", "287500.00"]
    sup_sign_conv = sum(sup_orig_vals.get(k, 0) for k in sup_sign_conv_keys)
    v["sup_total_originated"] = sup_total
    v["sup_const_1"] = sup_const_1
    v["sup_remaining"] = sup_remaining
    v["sup_sign_conv"] = sup_sign_conv
    v["sup_entries"] = len(sup_results)

    # F5 narrative: sign-inv originated values and exclusion count
    # "75 originated operand values that are sign-inversions by value"
    # Exclude: outcomes (not values) for provenance reporting
    v["a_excl_sign_originated"] = (
        v["a_prov_originated"]
        - v["a_outcomes_sign_inv"]
    )

    # F6 item-level breakdown
    # F6 dynamic per-item summary (§2 of the F6 fix)
    MECH_LABELS = {
        "sign_inv": ("sign inversion", "sign inversions"),
        "ungrounded": ("ungrounded chain", "ungrounded chain"),
        "untraceable": ("untraceable", "untraceable"),
    }
    # Build breakdown from per-item-per-mechanism variables
    f6_items = {}
    for key, val in v.items():
        m = re.match(r"a_orig_item_(Q\d+)_(sign_inv|ungrounded|untraceable)$", key)
        if m:
            item_id, mech = m.group(1), m.group(2)
            f6_items.setdefault(item_id, {})[mech] = val
    # Sort by total descending, then by item_id ascending for ties
    sorted_items = sorted(
        f6_items.items(),
        key=lambda kv: (-sum(kv[1].values()), kv[0]),
    )
    n_items = len(sorted_items)
    if n_items == 0:
        v["f6_per_item_summary"] = "No originated outcomes were observed."
    else:
        item_word = "item" if n_items == 1 else "items"
        summary_lines = [
            f"Total: {v['a_total_originated_operands']} originated operand "
            f"values, concentrated on {n_items} {item_word}."
        ]
        for item_id, mechs in sorted_items:
            total = sum(mechs.values())
            parts = []
            for mech_key in ("sign_inv", "ungrounded", "untraceable"):
                count = mechs.get(mech_key, 0)
                if count > 0:
                    singular, plural = MECH_LABELS[mech_key]
                    label = singular if count == 1 else plural
                    parts.append(f"{count} {label}")
            summary_lines.append(f"{item_id}: {total} ({' + '.join(parts)}).")
        v["f6_per_item_summary"] = "\n".join(summary_lines)

    return v


def generate(values=None, template_path=None, target_path=None):
    """Generate FINDINGS.md from template and computed values.

    Returns the generated text. If target_path is given, writes to file.
    """
    if values is None:
        values = compute_figures()
    if template_path is None:
        template_path = TEMPLATE

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Find all placeholders
    placeholders = set(re.findall(r"\{\{(\w+)\}\}", template))

    # Check for missing values
    missing = placeholders - set(values.keys())
    if missing:
        print(f"FATAL: {len(missing)} placeholders have no computed value:", file=sys.stderr)
        for m in sorted(missing):
            print(f"  {{{{{m}}}}}", file=sys.stderr)
        sys.exit(1)

    # Check for unused values
    used = set()
    def replace_placeholder(match):
        key = match.group(1)
        used.add(key)
        val = values[key]
        if isinstance(val, int):
            return f"{val:,}"
        elif isinstance(val, Decimal):
            return str(val)
        return str(val)

    result = re.sub(r"\{\{(\w+)\}\}", replace_placeholder, template)

    # Report unused (excluding internal-only keys)
    internal_keys = {k for k in values if k.endswith("_vals") or k.startswith("sup_")}
    unused = set(values.keys()) - used - internal_keys
    # Filter out generated keys that are legitimately unused (per-item details etc)
    noise_prefixes = ("a_orig_", "b_orig_", "a_orig_item_", "b_orig_item_",
                      "a_d1_", "b_d1_", "a_step4_Q", "b_step4_")
    unused = {k for k in unused
              if not any(k.startswith(p) for p in noise_prefixes)
              and k not in ("a_base_count", "b_base_count", "a_ir_count",
                            "b_ir_count", "a_invoked_base", "b_invoked_base",
                            "a_invoked_ir", "b_invoked_ir", "a_correct_ops",
                            "b_correct_ops", "a_total_prov", "b_total_prov",
                            "a_total_entries", "b_total_entries",
                            "a_Q08_base_total", "b_Q08_base_total",
                            "a_wo_item_wrong", "b_wo_item_wrong",
                            )}
    if unused:
        print(f"WARNING: {len(unused)} computed values unused in template:", file=sys.stderr)
        for u in sorted(unused):
            print(f"  {u} = {values[u]}", file=sys.stderr)

    if target_path:
        with open(target_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(result)

    return result


def main():
    values = compute_figures()
    result = generate(values, target_path=TARGET)
    lines = result.count("\n")
    print(f"Generated FINDINGS.md: {lines} lines, {len(result.encode('utf-8'))} bytes")
    print(f"  Computed {len(values)} values")


if __name__ == "__main__":
    main()
