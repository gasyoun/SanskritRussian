# README.meta.md — companion metadoc for the SanskritRussian README

_Created: 20-07-2026 · Last updated: 20-07-2026_

Metadoc for [README.md](https://github.com/gasyoun/SanskritRussian/blob/main/README.md), the
**canonical documentation** of the Sanskrit→Russian gloss layer. Onboarding pack a fresh
session would otherwise rediscover by trial and error.

## Purpose

The single authoritative description of the three-layer Sa→Ru glossary — method, coverage,
failure typology, and the **coverage ≠ accuracy** caveat. Per decision **D11** (H1349 plan),
this repo owns method/coverage/typology/accuracy; the generation-pipeline README in
[`SanskritLexicography/RussianTranslation/glossary/README.md`](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/glossary/README.md)
is a build runbook that points here.

## Audience

Researchers and learners consuming the published glossary + the live site; secondarily, an
agent maintaining the layer. Data lives in this repo; the pipeline lives in SanskritLexicography.

## Provenance

- Layer built by the pipeline described in the [PLAN](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/docs/PLAN_RussianTranslation_saru-gloss-quality_2026H2.md)
  (handoff [H1349](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1349-Opus_RussianTranslation_saru-gloss-quality-uplift_19.07.26.md)).
- Doc consolidation + the coverage≠accuracy caveat: H1349 wave 1, 20-07-2026, Opus 4.8 (`claude-opus-4-8`).

## Load-bearing facts / limitations

- **The published data is one generation behind the fixed pipeline.** The tables here (e.g.
  **2,021 roots**, coverage 42.4/57.4/58.7 %) describe the *currently published* `.tsv`/`.jsonl`.
  The H1349 wave-1 pipeline fixes (pseudo-root split, homograph trail, vidyut ambiguity trail)
  are **not** yet republished — republish is fenced behind a human GO (**D8**). A wave-2-gated
  republish will drop the root count to **~1,853** and refresh the coverage/typology tables.
- **Coverage ≠ accuracy.** 87.1 % is a resolution rate; the accuracy ceiling is the 84.4 %
  upstream pair precision, compounded by an unvalidated lemmatization join. A measured per-tier
  precision figure lands in **wave 2**.
- **`√gam` showcase numbers** (678 forms / 44 lemmas / 7,116 occ; пришел 196 · отправился 177 · …)
  are reconciled to the current-data regen across README / USE_CASES / SAMPLE (H1349 W1.4).

## Improvement backlog (ranked)

1. **Wave 2 — measured per-tier precision** (DCS / Vidyut / marker × frequency). Turns the
   caveat into a number; the single highest-value follow-up.
2. **Republish (D8, human-gated)** the fixed data, then update the root count (2,021→~1,853),
   coverage, and typology tables here in the same pass.
3. **Expose homograph / vidyut alternates in `index.html`** — the trails are now fully captured
   (`ambiguity_homographs.tsv`, `vidyut_ambiguity.tsv`); the UI still shows only the dominant lemma.
4. **Coverage via `vidyut.cheda`** (wave 3) for the 48,646 unrecognized simplexes / 20,823 long
   compounds — reflect any recovered-form deltas here.

## Revision history

| Date | Change | By |
|---|---|---|
| 20-07-2026 | Metadoc created; caveat + `√gam` reconciliation added to README (H1349 W1.4/W1.5). | Opus 4.8 (`claude-opus-4-8`) |

_Dr. Mārcis Gasūns_
