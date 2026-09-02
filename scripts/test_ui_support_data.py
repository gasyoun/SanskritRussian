#!/usr/bin/env python
"""test_ui_support_data.py — H3877 data-contract tests.

Minimal, dependency-free checks that the UI-support sidecar files
(lemma_provenance.tsv, root_provenance.tsv, lemma_ambiguity.tsv,
vidyut_ambiguity.tsv) have the schema and row-count parity index.html's
JS (parseProvenance/parseAmbiguity/load) assumes, and that every key they
reference exists in the corresponding published glossary. Run from the
repo root:

    python scripts/test_ui_support_data.py

Exits non-zero on any failure.
"""
import csv
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
        print(f"FAIL: {msg}")
    else:
        print(f"ok:   {msg}")


def load_jsonl_keys(path, key_field):
    keys = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            keys.add(json.loads(line)[key_field])
    return keys


def load_tsv_rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def test_provenance(jsonl_name, key_field, tsv_name):
    jsonl_path = os.path.join(REPO, jsonl_name)
    tsv_path = os.path.join(REPO, tsv_name)
    keys = load_jsonl_keys(jsonl_path, key_field)
    rows = load_tsv_rows(tsv_path)
    check(
        {"source", "registers"} <= set(rows[0].keys()) if rows else False,
        f"{tsv_name} has columns {key_field},source,registers",
    )
    check(
        len(rows) == len(keys),
        f"{tsv_name} row count ({len(rows)}) == {jsonl_name} entry count ({len(keys)})",
    )
    tsv_keys = {r[key_field] for r in rows}
    check(
        tsv_keys == keys,
        f"{tsv_name} keys are exactly the {jsonl_name} keys (no drift)",
    )
    check(
        all(r["source"] for r in rows),
        f"every {tsv_name} row has a non-empty source field",
    )


def test_ambiguity():
    path = os.path.join(REPO, "lemma_ambiguity.tsv")
    rows = load_tsv_rows(path)
    check(
        {"lemma_slp1", "n_ambiguous_forms", "sample"} <= set(rows[0].keys()) if rows else False,
        "lemma_ambiguity.tsv has columns lemma_slp1,n_ambiguous_forms,sample",
    )
    lemma_keys = load_jsonl_keys(os.path.join(REPO, "lemma_glossary.jsonl"), "lemma_slp1")
    stray = [r["lemma_slp1"] for r in rows if r["lemma_slp1"] not in lemma_keys]
    check(not stray, f"every lemma_ambiguity.tsv key exists in lemma_glossary.jsonl (stray: {stray[:5]})")
    check(
        all(int(r["n_ambiguous_forms"]) >= 1 for r in rows),
        "every lemma_ambiguity.tsv row has n_ambiguous_forms >= 1",
    )


def test_vidyut_ambiguity():
    path = os.path.join(REPO, "vidyut_ambiguity.tsv")
    rows = load_tsv_rows(path)
    expected_cols = {"form_slp1", "primary_lemma", "primary_pos", "primary_n", "alt_lemma", "alt_pos", "alt_n"}
    check(
        expected_cols <= set(rows[0].keys()) if rows else False,
        f"vidyut_ambiguity.tsv has columns {sorted(expected_cols)}",
    )
    # Reconciliation contract: every primary (lemma,pos) pick must agree with
    # the published vidyut_form2lemma.tsv baseline (H3877 evidence step).
    published = {}
    with open(os.path.join(REPO, "vidyut_form2lemma.tsv"), encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            published[row["form_slp1"]] = (row["lemma_slp1"], row["pos"])
    mismatches = [
        r["form_slp1"] for r in rows
        if published.get(r["form_slp1"]) != (r["primary_lemma"], r["primary_pos"])
    ]
    check(
        not mismatches,
        f"every vidyut_ambiguity.tsv primary pick agrees with published vidyut_form2lemma.tsv (mismatches: {mismatches[:5]})",
    )
    check(len(rows) > 0, "vidyut_ambiguity.tsv is non-empty")


def test_index_html_wiring():
    html = open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
    for needle in (
        "parseProvenance", "parseAmbiguity", "_provenance.tsv",
        "lemma_ambiguity.tsv", "ambiguity_homographs.tsv", "vidyut_ambiguity.tsv",
    ):
        check(needle in html, f"index.html references {needle!r}")


def main():
    test_provenance("lemma_glossary.jsonl", "lemma_slp1", "lemma_provenance.tsv")
    test_provenance("root_glossary.jsonl", "root_slp1", "root_provenance.tsv")
    test_ambiguity()
    test_vidyut_ambiguity()
    test_index_html_wiring()

    print()
    if failures:
        print(f"{len(failures)} FAILURE(S)")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
