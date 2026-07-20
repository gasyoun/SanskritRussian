# Changelog

_Created: 01-07-2026 · Last updated: 20-07-2026_

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning is
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/gasyoun/SanskritRussian/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/gasyoun/SanskritRussian/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/gasyoun/SanskritRussian/releases/tag/v1.0.0

_Dr. Mārcis Gasūns_
