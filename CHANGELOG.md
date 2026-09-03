# Changelog

_Created: 01-07-2026 · Last updated: 03-09-2026_

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning is
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- **Marker-residual recovery measured and documented (H3876, 03-09-2026).** The pipeline in the
  sibling repo now recovers **1,018 of the 1,389 marker-residual forms / 1,783 of the 2,312
  tokens** by lemmatizing a compound's rightmost element through the DCS form→lemma map
  (`source='marker-head'` — a separate tier tag, because this is the layer's weakest evidence
  and must stay filterable). `A-brahma-BuvanAt` was unresolved only because `BuvanAt` is an
  *ablative of* `Buvana`, in neither the bare-root nor the bare-lemma inventory but a DCS form
  key all along; nothing is segmented, so the wave-3 `vidyut.cheda` NO-GO stands. **Data here is
  unchanged** — republish stays fenced behind the human D8 gate, and the README now carries a
  pending-republish note with the numbers it will land: coverage 87.11 % → **87.28 %**, resolved
  forms 111,996 → 113,014, typology row 1,389/2,312 → **371/529**, roots 1,853 → 1,856.
  Lemma precision 25/25 on the canonical tier × frequency sample (single-judge; the 3-judge
  panel run is still owed) against the wave-2 `marker` baseline of 93.3 %; 27 of 40,387 lemma
  entries change their dominant Russian rendering, 23 of those ties between two one-occurrence
  glosses. Honest weak point: a compound's Russian attaches to its head lemma, so a bahuvrīhi
  (`vigata-BIr` "бесстрашный" → `BI` "страх") is mis-attributed — the wave-2 panel's systematic
  lemma defect #3, extended, not solved. `README.meta.md` backlog reconciled against what
  actually shipped. Report:
  [REPORT_H3876_saru_marker_head_recovery_03-09-2026.md](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/docs/REPORT_H3876_saru_marker_head_recovery_03-09-2026.md).
  Opus 5 (`claude-opus-5`).

## [1.3.0] — 2026-09-02

### Added
- **Provenance + homograph UI (H3877).** `index.html` now fetches and displays each
  lemma/root card's `source` (dcs/vidyut/marker) and top-3 `registers` breakdown, and flags
  lemmas with contested alternate lemmas (⚠ contested form indicator, sourced from both the
  DCS-tier `ambiguity_homographs.tsv` and the newly-published Vidyut-tier
  `vidyut_ambiguity.tsv`) instead of silently showing only the dominant lemma. New small,
  bounded sidecar files: [`lemma_provenance.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/lemma_provenance.tsv),
  [`root_provenance.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/root_provenance.tsv),
  [`lemma_ambiguity.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/lemma_ambiguity.tsv),
  [`vidyut_ambiguity.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/vidyut_ambiguity.tsv)
  (mirrors `ambiguity_homographs.tsv`'s schema for the Vidyut tier; designed in the sibling
  pipeline's `build_vidyut_fallback.py` but never previously generated/published — see
  [README](https://github.com/gasyoun/SanskritRussian/blob/main/README.md#files) for the
  reconciliation-against-baseline note). Generators + data-contract tests added under
  [`scripts/`](https://github.com/gasyoun/SanskritRussian/tree/main/scripts). No existing
  glossary `.tsv`/`.jsonl` file touched.

## [1.2.1] — 2026-08-04

### Changed
- **Curated root-gloss surfaces converted to the citation register** (H2290, the sweep
  H1860 deferred): [SAMPLE_root_glossary.md](https://github.com/gasyoun/SanskritRussian/blob/main/SAMPLE_root_glossary.md)
  now carries an authored dictionary-neutral **Citation gloss** line per showcased root (7
  roots) plus a data-framing note; the [README](https://github.com/gasyoun/SanskritRussian/blob/main/README.md)
  `√gam` example and [USE_CASES.md](https://github.com/gasyoun/SanskritRussian/blob/main/USE_CASES.md)
  §1 now distinguish quoted corpus data from the authored citation gloss. Corpus rollup
  data untouched; `index.html` had no headline glosses (verified).

## [1.2.0] — 2026-08-04

### Added
- **[ROOT_GLOSS_REGISTER_POLICY.md](https://github.com/gasyoun/SanskritRussian/blob/main/ROOT_GLOSS_REGISTER_POLICY.md)** (+ metadoc) — the register standard for authored Russian citation glosses of verb roots (H1860): dictionary-neutral infinitives, explicit person/aspect/voice rule, 18 worked examples from `root_glossary.tsv`, and a measured inconsistency census (top-1 infinitive share 5.8 %; 678/1,205 roots mix ≥2 register classes). Linked from the README; governs curated glosses only — the generated rollup data is untouched.

## [1.1.1] — 2026-07-20

### Added
- **Coverage ≠ accuracy caveat** on the README and the live [`index.html`](https://github.com/gasyoun/SanskritRussian/blob/main/index.html):
  the 87.1 % headline is a *resolution* rate, not a correctness rate; the accuracy ceiling is the
  84.4 % upstream pair precision, compounded by an as-yet-unvalidated lemmatization join; a
  measured per-tier precision figure is coming in wave 2 (H1349 W1.5).
- **[README.meta.md](https://github.com/gasyoun/SanskritRussian/blob/main/README.meta.md)** companion
  metadoc: purpose, provenance, load-bearing limitations, ranked improvement backlog.

### Changed
- README is now the **canonical** method/coverage/typology/accuracy doc (D11); the pipeline
  `glossary/README.md` in SanskritLexicography shrank to a build runbook pointing here.
- `√gam` showcase numbers reconciled to the current-data regen across README / USE_CASES /
  SAMPLE (пришел 196 · отправился 177 · ушел 141 …; direction unchanged) (H1349 W1.4).

### Note
- Published data (`.tsv`/`.jsonl`) is **unchanged** — the H1349 wave-1 pipeline fixes are not yet
  republished (republish is human-gated, D8). A later republish drops the root count 2,021 → ~1,853.

## [1.1.0] — 2026-07-12

### Added
- Course CTA footer on the live glossary page ([H716](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H716-Fable_SanskritKaraoke_free-funnel-cta-audit_11.07.26.md)
  free-funnel audit): «Смотреть актуальные курсы санскрита →» → `samskrte.ru/online` with
  `utm_source=glossary&utm_medium=cta&utm_campaign=sanskritrussian`, custdev-proven hint
  «Можно в записи и в своём темпе», secondary «Задать вопрос в Telegram» → `t.me/rusamskrtam`.
  Audit table lives in [SanskritKaraoke docs/FREE_FUNNEL_CTA_AUDIT_07_2026.md](https://github.com/gasyoun/SanskritKaraoke/blob/main/docs/FREE_FUNNEL_CTA_AUDIT_07_2026.md).

## [1.0.1] — 2026-07-01

### Added
- [`INTERLINKS.md`](https://github.com/gasyoun/SanskritRussian/blob/main/INTERLINKS.md) — how the
  glossary connects upstream (corpus_lexicon, VisualDCS, vidyut) and to potential downstream
  consumers (PWG/MW→RU kits, WhitneyRoots root crosswalk, VisualDCS, SanskritKaraoke, BookIndex,
  VedaWeb, csl-atlas). Registered in the cross-repo hub `Uprava/PROJECT_INTERLINKS.md`.

## [1.0.0] — 2026-07-01

Initial public release — the three-layer Sanskrit→Russian glossary, data + live site.

### Added
- **Surface layer** — 190,838 attested forms → ranked Russian renderings with counts,
  registers, works, kinds ([`surface_glossary.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/surface_glossary.tsv);
  the 140 MB JSONL ships as [`.gz`](https://github.com/gasyoun/SanskritRussian/blob/main/surface_glossary.jsonl.gz)
  + a per-initial-letter split under [`surface/`](https://github.com/gasyoun/SanskritRussian/tree/main/surface), 26 parts).
- **Lemma layer** — 40,370 stems/verb-lemmas → Russian
  ([`lemma_glossary.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/lemma_glossary.tsv)).
- **Root layer** — 2,021 verb roots aggregated over all forms & prefixed verbs
  ([`root_glossary.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/root_glossary.tsv)); e.g. `√gam` →
  678 forms / 44 lemmas / 7,116 occ.
- **Lemmatization join** — DCS `form→lemma` (root via longest DCS-root suffix) → Vidyut kosha
  fallback → morpheme-marker tier; **87.1 % token coverage**, provenance-tagged `dcs|vidyut|marker`.
- **Failure typology** + [`surface_unresolved.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/surface_unresolved.tsv)
  (78,842 unresolved forms) and [`ambiguity_homographs.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/ambiguity_homographs.tsv).
- **Searchable site** — [`index.html`](https://github.com/gasyoun/SanskritRussian/blob/main/index.html),
  client-side search by SLP1 or Russian with SLP1→IAST display; `.nojekyll` static serving.
- [`README.md`](https://github.com/gasyoun/SanskritRussian/blob/main/README.md) (method + typology),
  [`USE_CASES.md`](https://github.com/gasyoun/SanskritRussian/blob/main/USE_CASES.md),
  [`SAMPLE_root_glossary.md`](https://github.com/gasyoun/SanskritRussian/blob/main/SAMPLE_root_glossary.md).

### Fixed
- Windows case-insensitive-filesystem collision in per-letter bucketing (was losing 23,007 of
  190,838 records); bucket names are now case-folded to upper. Split verified lossless.

[Unreleased]: https://github.com/gasyoun/SanskritRussian/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/gasyoun/SanskritRussian/compare/v1.2.0...v1.2.1
[1.0.1]: https://github.com/gasyoun/SanskritRussian/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/gasyoun/SanskritRussian/releases/tag/v1.0.0

_Dr. Mārcis Gasūns_
