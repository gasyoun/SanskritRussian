#!/usr/bin/env python
"""reconcile_vidyut_ambiguity.py — H3877 evidence step.

`build_vidyut_fallback.py` in the sibling SanskritLexicography pipeline was
already designed to emit a `vidyut_ambiguity.tsv` mirroring
`ambiguity_homographs.tsv`'s schema, but that file had never actually been
generated/published in this repo. Regenerating it from a current `vidyut`
package install reproduces the published `vidyut_form2lemma.tsv`'s exact row
count (28,567) but not identical per-row primary-lemma picks — evidence of
`vidyut` kosha-data version drift since the original publish.

To avoid introducing a second, disagreeing lemmatization surface into the UI,
this script keeps only rows of a freshly-generated `vidyut_ambiguity.tsv`
(regenerated via the sibling pipeline's `build_vidyut_fallback.py` logic,
against `surface_dcs_misses.tsv`, into a scratch directory — NOT run inside
this repo or its tree) whose primary `(lemma, pos)` pick agrees with this
repo's already-published, trusted `vidyut_form2lemma.tsv`. The published
primary-lemma baseline is never altered; only alt-lemma trail data consistent
with it is kept.

Usage:
    python scripts/reconcile_vidyut_ambiguity.py <regenerated_vidyut_ambiguity.tsv> [--repo <repo_root>]

Writes <repo_root>/vidyut_ambiguity.tsv.
"""
import csv
import sys
import os
import argparse

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("regenerated", help="freshly-generated vidyut_ambiguity.tsv to reconcile")
    ap.add_argument("--repo", default=REPO, help="SanskritRussian repo root (default: this script's grandparent dir)")
    args = ap.parse_args()

    published_path = os.path.join(args.repo, "vidyut_form2lemma.tsv")
    out_path = os.path.join(args.repo, "vidyut_ambiguity.tsv")

    published = {}
    with open(published_path, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            published[row["form_slp1"]] = (row["lemma_slp1"], row["pos"])

    total = agree = kept_rows = 0
    with open(args.regenerated, encoding="utf-8") as f, \
         open(out_path, "w", encoding="utf-8", newline="\n") as out:
        r = csv.DictReader(f, delimiter="\t")
        w = csv.writer(out, delimiter="\t", lineterminator="\n")
        w.writerow(["form_slp1", "primary_lemma", "primary_pos", "primary_n",
                    "alt_lemma", "alt_pos", "alt_n"])
        seen_forms = set()
        for row in r:
            total += 1
            form = row["form_slp1"]
            pub = published.get(form)
            seen_forms.add(form)
            if pub and pub == (row["primary_lemma"], row["primary_pos"]):
                agree += 1
                w.writerow([row["form_slp1"], row["primary_lemma"], row["primary_pos"],
                            row["primary_n"], row["alt_lemma"], row["alt_pos"], row["alt_n"]])
                kept_rows += 1

    print(f"ambiguity-trail rows: {total}; forms touched: {len(seen_forms)}")
    print(f"rows whose primary matches published vidyut_form2lemma.tsv: {agree} ({100*agree/total:.1f}%)")
    print(f"reconciled file rows kept: {kept_rows} -> {out_path}")


if __name__ == "__main__":
    main()
