#!/usr/bin/env python3
"""H6061 — Semantic fields of the SanskritRussian RU layer vs the MW sense tree.

Joins this repo's lemma-level Russian translation distributions (Layer 2,
lemma_glossary.jsonl) against the kosha WordSem 3-layer gold (H1453:
WN synset / MW numbered sense / semdom) in data/frequency/sense_frequency.tsv.

Outputs (into analysis/):
  - semantic_fields_table.tsv  per-semdom coverage + richness table
  - ru_wsd_bridge.tsv          multi-field lemmas x RU translation distribution
                               (bridge input for WSD on RU translations, B11)
  - semantic_fields_stats.json machine-readable summary for the report

Determinism: pure stdlib, sorted iterations only; rerun must be byte-identical.

Usage:
  python3 scripts/build_semantic_fields_vs_mw.py \
      [--kosha-sense-frequency PATH] [--glossary PATH] [--outdir analysis]
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from collections import defaultdict

DEFAULT_KOSHA = os.path.expanduser(
    "~/Documents/GitHub/kosha/data/frequency/sense_frequency.tsv"
)
DEFAULT_GLOSSARY = "lemma_glossary.jsonl"


def shannon_entropy(counts: list[int]) -> float:
    total = sum(counts)
    if total <= 0:
        return 0.0
    h = 0.0
    for c in counts:
        p = c / total
        if p > 0:
            h -= p * math.log2(p)
    return h


def median(vals: list[float]) -> float:
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return 0.0
    m = n // 2
    if n % 2:
        return float(s[m])
    return (s[m - 1] + s[m]) / 2.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kosha-sense-frequency", default=DEFAULT_KOSHA)
    ap.add_argument("--glossary", default=DEFAULT_GLOSSARY)
    ap.add_argument("--outdir", default="analysis")
    args = ap.parse_args()

    # --- 1. kosha side: semdom fields + MW sense counts per lemma ---------
    lemma_fields: dict[str, dict[str, int]] = defaultdict(dict)  # lemma -> field -> count
    lemma_mw_senses: dict[str, int] = defaultdict(int)
    field_lemma_seen: set[tuple[str, str]] = set()
    with open(args.kosha_sense_frequency, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        col = {name: i for i, name in enumerate(header)}
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            lemma = parts[col["lemma_slp1"]]
            layer = parts[col["layer"]]
            if layer == "semdom":
                field = parts[col["sense_id"]]
                cnt = int(parts[col["count_all"]] or 0)
                if (lemma, field) not in field_lemma_seen:
                    field_lemma_seen.add((lemma, field))
                    lemma_fields[lemma][field] = cnt
            elif layer == "mw":
                lemma_mw_senses[lemma] += 1

    kosha_tagged = set(lemma_fields)

    # --- 2. RU side: translation distributions per lemma ------------------
    ru: dict[str, dict] = {}
    with open(args.glossary, encoding="utf-8") as fh:
        for line in fh:
            rec = json.loads(line)
            lemma = rec["lemma_slp1"]
            trans = rec.get("translations", [])
            counts = [t["n"] for t in trans]
            ru[lemma] = {
                "n": rec.get("n", sum(counts)),
                "distinct": len(trans),
                "entropy": shannon_entropy(counts),
                "top5": sorted(trans, key=lambda t: (-t["n"], t["ru"]))[:5],
            }

    # --- 3. join ----------------------------------------------------------
    matched = kosha_tagged & set(ru)
    coverage = len(matched) / len(kosha_tagged) * 100.0 if kosha_tagged else 0.0
    # corpus-attested subset: semdom-tagged lemmas that also carry mw-layer rows
    # (mw rows exist only for corpus-visible lemmas: ws attested or MFS-estimated
    # on DCS tokens) — the fair field-coverage denominator.
    attested_tagged = {l for l in kosha_tagged if lemma_mw_senses.get(l, 0) > 0}
    attested_matched = attested_tagged & set(ru)
    attested_coverage = (len(attested_matched) / len(attested_tagged) * 100.0
                         if attested_tagged else 0.0)
    # keying sanity floor: the full semdom population includes dictionary-only
    # lemmas (kosha FINDINGS 86: corpus is lacunar) so its floor is low; the
    # corpus-attested subset must match at >=60% or the join keying is broken.
    if coverage < 40.0 or attested_coverage < 60.0:
        print(f"CHECK FAIL: join coverage full={coverage:.1f}% (floor 40) "
              f"attested={attested_coverage:.1f}% (floor 60)",
              file=sys.stderr)
        return 2

    # per-lemma number of fields
    n_fields = {lem: len(f) for lem, f in lemma_fields.items()}

    # --- 4. per-field table ------------------------------------------------
    fields: dict[str, dict] = defaultdict(
        lambda: {"ws_lemmas": 0, "ru_matched": 0, "ru_tokens": 0,
                 "distinct": [], "entropy": [], "mw_senses": []})
    for lemma in kosha_tagged:
        for field in lemma_fields[lemma]:
            f = fields[field]
            f["ws_lemmas"] += 1
            if lemma in ru:
                r = ru[lemma]
                f["ru_matched"] += 1
                f["ru_tokens"] += r["n"]
                f["distinct"].append(r["distinct"])
                f["entropy"].append(r["entropy"])
                f["mw_senses"].append(lemma_mw_senses.get(lemma, 0))

    # gap thresholds computed on fields with >=20 tagged lemmas (stable set)
    major = {name for name, f in fields.items() if f["ws_lemmas"] >= 20}
    cov_vals = sorted(
        fields[name]["ru_matched"] / fields[name]["ws_lemmas"] * 100.0
        for name in major)
    distinct_vals = sorted(median(fields[name]["distinct"]) for name in major)

    def quartile(sorted_vals: list[float], k: int) -> float:
        if not sorted_vals:
            return 0.0
        idx = k * (len(sorted_vals) - 1) // 4
        return sorted_vals[idx]

    cov_q1 = quartile(cov_vals, 1)
    distinct_q1 = quartile(distinct_vals, 1)

    os.makedirs(args.outdir, exist_ok=True)
    table_path = os.path.join(args.outdir, "semantic_fields_table.tsv")
    with open(table_path, "w", encoding="utf-8") as out:
        out.write("semdom\tws_lemmas\tru_matched\tru_coverage_pct\tru_tokens\t"
                  "mw_senses_median\tru_distinct_median\tru_entropy_median\t"
                  "low_coverage\tthin_ru\n")
        for name in sorted(fields, key=lambda n: (-fields[n]["ws_lemmas"], n)):
            f = fields[name]
            cov = f["ru_matched"] / f["ws_lemmas"] * 100.0 if f["ws_lemmas"] else 0.0
            low_cov = name in major and cov <= cov_q1
            thin = (name in major
                    and median(f["distinct"]) <= distinct_q1
                    and f["ru_matched"] > 0)
            out.write(
                f"{name}\t{f['ws_lemmas']}\t{f['ru_matched']}\t{cov:.1f}\t"
                f"{f['ru_tokens']}\t{median(f['mw_senses']):.1f}\t"
                f"{median(f['distinct']):.1f}\t{median(f['entropy']):.2f}\t"
                f"{'YES' if low_cov else ''}\t{'YES' if thin else ''}\n")

    # --- 5. WSD bridge: multi-field lemmas with RU distributions ----------
    bridge_path = os.path.join(args.outdir, "ru_wsd_bridge.tsv")
    bridge_rows = []
    for lemma in matched:
        if n_fields[lemma] < 2:
            continue
        r = ru[lemma]
        flds = sorted(lemma_fields[lemma], key=lambda f: (-lemma_fields[lemma][f], f))
        top5 = "; ".join(f"{t['ru']}({t['n']})" for t in r["top5"])
        bridge_rows.append(
            (lemma, n_fields[lemma], "|".join(flds),
             lemma_mw_senses.get(lemma, 0), r["n"], r["distinct"],
             f"{r['entropy']:.3f}", top5))
    bridge_rows.sort(key=lambda row: (-row[4], row[0]))
    with open(bridge_path, "w", encoding="utf-8") as out:
        out.write("lemma_slp1\tn_fields\tfields\tmw_senses\tru_tokens\t"
                  "ru_distinct\tru_entropy\ttop5_ru\n")
        for row in bridge_rows:
            out.write("\t".join(str(x) for x in row) + "\n")

    # --- 6. mono vs multi-field RU variability (WSD motivation) -----------
    mono_d, mono_e, multi_d, multi_e = [], [], [], []
    for lemma in matched:
        r = ru[lemma]
        if n_fields[lemma] == 1:
            mono_d.append(r["distinct"]); mono_e.append(r["entropy"])
        else:
            multi_d.append(r["distinct"]); multi_e.append(r["entropy"])

    # --- 7. RU-richer side: RU lemmas with no semdom tag ------------------
    untagged = [lem for lem in ru if lem not in kosha_tagged]
    untagged_sorted = sorted(untagged, key=lambda l: (-ru[l]["n"], l))

    stats = {
        "kosha_tagged_lemmas": len(kosha_tagged),
        "attested_tagged_lemmas": len(attested_tagged),
        "attested_matched_lemmas": len(attested_matched),
        "attested_join_coverage_pct": round(attested_coverage, 2),
        "ru_lemmas": len(ru),
        "matched_lemmas": len(matched),
        "join_coverage_pct": round(coverage, 2),
        "n_fields_total": len(fields),
        "fields_ge20_lemmas": len(major),
        "coverage_q1_pct_major": round(cov_q1, 2),
        "distinct_q1_major": round(distinct_q1, 2),
        "mono_field_lemmas": len(mono_d),
        "multi_field_lemmas": len(multi_d),
        "mono_distinct_median": round(median(mono_d), 2),
        "multi_distinct_median": round(median(multi_d), 2),
        "mono_entropy_median": round(median(mono_e), 3),
        "multi_entropy_median": round(median(multi_e), 3),
        "ru_untagged_lemmas": len(untagged),
        "ru_untagged_top20_tokens": [
            {"lemma": l, "n": ru[l]["n"]} for l in untagged_sorted[:20]],
        "bridge_rows": len(bridge_rows),
    }
    stats_path = os.path.join(args.outdir, "semantic_fields_stats.json")
    with open(stats_path, "w", encoding="utf-8") as out:
        json.dump(stats, out, ensure_ascii=False, indent=1, sort_keys=True)
        out.write("\n")

    print(json.dumps(stats, ensure_ascii=False, indent=1, sort_keys=True))
    print(f"\nwrote {table_path}, {bridge_path}, {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
