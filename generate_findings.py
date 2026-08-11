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
        outcomes_sign_inv = 0
        outcomes_ungrounded = 0
        outcomes_untraceable = 0
        for r in results:
            for p in r.get("provenance_results", []):
                if p["outcome"] != "OPERAND-ORIGINATED":
                    continue
                has_cis = any(
                    res.get("resolution") == "computed_in_session_ungrounded"
                    for res in p.get("operand_resolutions", [])
                )
                has_sign = any(
                    res.get("sign_inversion_finding") not in (None, False)
                    for res in p.get("operand_resolutions", [])
                )
                if has_cis:
                    outcomes_ungrounded += 1
                elif has_sign:
                    outcomes_sign_inv += 1
                else:
                    outcomes_untraceable += 1
        v[f"{pfx}_outcomes_sign_inv"] = outcomes_sign_inv
        v[f"{pfx}_outcomes_ungrounded"] = outcomes_ungrounded
        v[f"{pfx}_outcomes_untraceable"] = outcomes_untraceable

        # Originated by item
        orig_items = defaultdict(int)
        for r in results:
            for p in r.get("provenance_results", []):
                if p["outcome"] == "OPERAND-ORIGINATED":
                    orig_items[r["item_id"]] += 1
        for item, count in orig_items.items():
            v[f"{pfx}_orig_item_{item}"] = count

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
    v["f6_q09_originated"] = v.get("a_orig_item_Q09", 0)
    v["f6_q05_originated"] = v.get("a_orig_item_Q05", 0)

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
