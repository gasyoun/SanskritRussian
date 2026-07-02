# Interlinks — where this glossary sits in the ecosystem

_Created: 01-07-2026 · Last updated: 01-07-2026_

This repo is a **derived data asset**: it consumes three upstream sources through a pipeline
that lives in another repo, and it can feed several downstream consumers. Registered in the
cross-repo hub [`Uprava/PROJECT_INTERLINKS.md`](https://github.com/gasyoun/Uprava/blob/main/PROJECT_INTERLINKS.md).

```
 corpus_lexicon.jsonl ─┐
 (SanskritLexicography)│
                       │   pipeline (SanskritLexicography/RussianTranslation/src)
 dcs_full.sqlite ──────┼──▶  build_dcs_maps → build_surface_glossary  ──▶  THIS REPO
 (VisualDCS)           │     build_vidyut_fallback → build_rollup           (data + live site)
                       │                                                        │
 vidyut.kosha ─────────┘                                          ┌─────────────┴───────────────┐
 (ambuda-org, external)                                    translation memory / validation · root
                                                           crosswalks · RU gloss layers (below)
```

## Upstream — what it is built from (consume, don't rebuild)

| Source | Repo | Role |
|---|---|---|
| [`corpus_lexicon.jsonl`](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/src/corpus_lexicon.jsonl) | `gasyoun/SanskritLexicography` | the 1.09M word-aligned Sa→Ru tokens — the raw material (itself derived from [`SamudraManthanam`](https://github.com/gasyoun/SamudraManthanam), samskrtam.ru) |
| `dcs_full.sqlite` | [`gasyoun/VisualDCS`](https://github.com/gasyoun/VisualDCS/tree/main/src/DCS-data-2026) | DCS morphology (5.69M tokens) — the primary `form→lemma` join backbone |
| `vidyut.kosha` | [`ambuda-org/vidyut`](https://github.com/ambuda-org/vidyut) (external, pip) | Pāṇinian FST — the fallback lemmatizer for DCS misses |
| `indic_transliteration.sanscript` | external (pip) | IAST→SLP1 transcoding |

**Pipeline home:** the generation scripts are **not** in this repo — they live in
[`SanskritLexicography/RussianTranslation/src`](https://github.com/gasyoun/SanskritLexicography/tree/master/RussianTranslation/src)
(`build_dcs_maps.py` → `build_surface_glossary.py` → `build_vidyut_fallback.py` →
`build_rollup_glossaries.py`). Edit the pipeline there; the regenerated data is copied here.

## Toolchain (shared code)

- [`sanskrit-util`](https://github.com/gasyoun/sanskrit-util) is the org's canonical
  IAST⇄SLP1⇄Devanāgarī transcoder + normalization keys. This pipeline currently uses
  `indic_transliteration`; a future consolidation onto `sanskrit-util` is the natural cleanup
  (see [`SHARED_CODE.md`](https://github.com/gasyoun/SanskritLexicography/blob/master/SHARED_CODE.md)).

## Downstream — who could consume this (potential links, mostly not yet wired)

| Consumer | Repo | How it could use the glossary |
|---|---|---|
| PWG→RU / MW→RU kits | [`SanskritLexicography/RussianTranslation`](https://github.com/gasyoun/SanskritLexicography/tree/master/RussianTranslation) | as a **translation memory** / validation set — a form's attested Russian renderings prime or check machine output |
| SanskritKaraoke | [`gasyoun/SanskritKaraoke`](https://github.com/gasyoun/SanskritKaraoke) | RU gloss layer per verse (already wired **directly from `corpus_lexicon`**; the root-level glossary could enrich lemma glosses) |
| WhitneyRoots | [`gasyoun/WhitneyRoots`](https://github.com/gasyoun/WhitneyRoots) | join the **root layer** (`root_glossary.tsv`) to the Whitney-root crosswalk → a Russian gloss per √root, keyed by the shared root inventory / `mw_roots.tsv` |
| VisualDCS | [`gasyoun/VisualDCS`](https://github.com/gasyoun/VisualDCS) | reverse the join — attach the Russian gloss set back onto DCS lemmas for the DCS dashboards |
| BookIndex / Zaliznyak | [`gasyoun/BookIndex`](https://github.com/gasyoun/BookIndex) | the nominal (lemma) layer maps onto a Zaliznyak-style Russian grammatical index (Russian side) |
| VedaWeb | external (UZH, CC BY) | cross-check the Vedic-register slice against accented Rigveda morphology |
| csl-atlas | [`sanskrit-lexicon/csl-atlas`](https://github.com/sanskrit-lexicon/csl-atlas) | add a Russian-gloss column to the cross-dictionary headword atlas |

## Reuse rule

Before deriving *another* Sa→Ru signal (alignment table, root gloss index, frequency of Russian
equivalents), **query this repo's TSVs first** — that's the point of registering it in the hub.
The join keys are SLP1 throughout, matching the rest of the ecosystem.

_Dr. Mārcis Gasūns_
