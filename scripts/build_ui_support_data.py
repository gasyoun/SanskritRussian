#!/usr/bin/env python
"""build_ui_support_data.py — H3877 UI-support artifact generator.

Reads ONLY already-published SanskritRussian files (lemma_glossary.jsonl,
root_glossary.jsonl, ambiguity_homographs.tsv, and vidyut_ambiguity.tsv) and
derives three small, bounded sidecar TSVs for index.html to fetch alongside
the existing root/lemma TSVs:

  lemma_provenance.tsv   lemma_slp1, source, registers   (40,370 rows)
  root_provenance.tsv    root_slp1,  source, registers   (2,021 rows)
  lemma_ambiguity.tsv    lemma_slp1, n_ambiguous_forms, sample
                          (lemmas whose forms compete with an alt lemma in
                          DCS ambiguity_homographs.tsv and/or the Vidyut-tier
                          vidyut_ambiguity.tsv)

Does NOT touch any existing glossary .tsv/.jsonl file (repo's own downstream-
only rule, see CLAUDE.md) — these are new, additive artifacts only. Run from
anywhere; defaults to writing into the repo root next to this script's
grandparent directory. Regenerate with:

    python scripts/build_ui_support_data.py

then check with `python scripts/test_ui_support_data.py`.
"""
import sys
import os
import json
import csv
import collections
import argparse

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fmt_counts(d, topn=None):
    items = sorted(d.items(), key=lambda kv: -kv[1])
    if topn:
        items = items[:topn]
    return ",".join(f"{k}:{v}" for k, v in items)


def build_provenance(jsonl_path, key_field, out_path):
    n = 0
    with open(jsonl_path, encoding="utf-8") as f, \
         open(out_path, "w", encoding="utf-8", newline="\n") as out:
        out.write(f"{key_field}\tsource\tregisters\n")
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            key = rec[key_field]
            source = fmt_counts(rec.get("source", {}))
            registers = fmt_counts(rec.get("registers", {}), topn=3)
            out.write(f"{key}\t{source}\t{registers}\n")
            n += 1
    print(f"[provenance] {out_path}: {n} rows", file=sys.stderr)


def build_lemma_ambiguity(dcs_amb_path, vidyut_amb_path, out_path):
    # aggregate by primary_lemma: which forms of this lemma are contested
    by_lemma = collections.defaultdict(list)

    def load(path, tier):
        if not os.path.exists(path):
            print(f"[ambiguity] skip {tier}: {path} not found", file=sys.stderr)
            return
        with open(path, encoding="utf-8") as f:
            r = csv.DictReader(f, delimiter="\t")
            for row in r:
                by_lemma[row["primary_lemma"]].append(
                    (tier, row["form_slp1"], row["alt_lemma"],
                     row.get("alt_pos", row.get("alt_upos", "")), row["alt_n"])
                )

    load(dcs_amb_path, "dcs")
    load(vidyut_amb_path, "vidyut")

    n = 0
    with open(out_path, "w", encoding="utf-8", newline="\n") as out:
        out.write("lemma_slp1\tn_ambiguous_forms\tsample\n")
        for lemma, entries in sorted(by_lemma.items()):
            sample = ";".join(
                f"{tier}:{form}~{alt_lem}({alt_pos},{alt_n})"
                for tier, form, alt_lem, alt_pos, alt_n in entries[:5]
            )
            out.write(f"{lemma}\t{len(entries)}\t{sample}\n")
            n += 1
    print(f"[ambiguity] {out_path}: {n} lemma rows", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default=REPO, help="SanskritRussian repo root (default: this script's grandparent dir)")
    args = ap.parse_args()
    repo = args.repo

    build_provenance(
        os.path.join(repo, "lemma_glossary.jsonl"), "lemma_slp1",
        os.path.join(repo, "lemma_provenance.tsv"),
    )
    build_provenance(
        os.path.join(repo, "root_glossary.jsonl"), "root_slp1",
        os.path.join(repo, "root_provenance.tsv"),
    )
    build_lemma_ambiguity(
        os.path.join(repo, "ambiguity_homographs.tsv"),
        os.path.join(repo, "vidyut_ambiguity.tsv"),
        os.path.join(repo, "lemma_ambiguity.tsv"),
    )


if __name__ == "__main__":
    main()
