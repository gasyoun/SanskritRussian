# README.meta.md — companion metadoc for the SanskritRussian README

_Created: 20-07-2026 · Last updated: 03-09-2026_

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

- **The published data is now two generations behind the pipeline.** The tables here (e.g.
  **2,021 roots**, coverage 42.4/57.4/58.7 %) describe the *currently published* `.tsv`/`.jsonl`.
  Unreleased in the pipeline: (a) the H1349 wave-1 fixes (pseudo-root split, homograph trail,
  vidyut ambiguity trail), and (b) H3876's `marker-head` tier. Republish is fenced behind a
  human GO (**D8**) and will land both at once: root count **2,021 → 1,853** (from a) *and*
  **1,856** (+3 from b), resolved forms 111,996 → **113,014**, token coverage 87.11 % →
  **87.28 %**, the marker-residual typology row 1,389/2,312 → **371/529**. Anyone refreshing
  the tables must apply both deltas, not just the older one.
- **Coverage ≠ accuracy.** 87.1 % is a resolution rate; the accuracy ceiling is the 84.4 %
  upstream pair precision, compounded by an unvalidated lemmatization join. A measured per-tier
  precision figure lands in **wave 2**.
- **`√gam` showcase numbers** (678 forms / 44 lemmas / 7,116 occ; пришел 196 · отправился 177 · …)
  are reconciled to the current-data regen across README / USE_CASES / SAMPLE (H1349 W1.4).

## Improvement backlog (ranked)

1. ~~**Wave 2 — measured per-tier precision**~~ — **DONE 20-07-2026.** 3-judge panel, n=110:
   lemmatization 86.1 %, gloss 85.3 %; per tier dcs 94.9 % · vidyut 71.8 % · marker 93.3 %
   ([gold/saru_gloss_precision_report.md](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/gold/saru_gloss_precision_report.md)).
   Model-vs-model, not a human gold set — the human spot-check slot is still open.
2. **Republish (D8, human-gated)** the fixed data, then update the root count (2,021→1,856),
   coverage (87.11→87.28 %), and typology tables here in the same pass. **Two generations of
   pipeline change now ride on this one gate** (H1349 wave 1 + H3876) — see the load-bearing
   facts above.
3. ~~**Expose homograph / vidyut alternates in `index.html`**~~ — **DONE 02-09-2026** (H3877,
   v1.3.0: provenance, register breakdown and homograph alternates all render per entry).
4. ~~**Coverage via `vidyut.cheda`** (wave 3)~~ — **NO-GO, measured 20-07-2026**: 36.4 % coverage
   at 28 % segmentation / 18 % gloss precision, because a running-text segmenter shatters an
   isolated inflected form into a stem plus a spurious glossable particle
   ([gold/saru_gloss_wave3_cheda_coverage.md](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/gold/saru_gloss_wave3_cheda_coverage.md)).
   The long-compound stratum waits on a context-aware **neural** segmenter over the aligned
   verse text ("wave 3.5"), not on `vidyut.cheda` over isolated forms. **Do not re-propose it.**
5. **A 3-judge panel on the new `marker-head` stratum** (H3876). The tier is registered in the
   `TIERS` tuple of the sampler and aggregator, so the next panel run picks it up with no code
   change; the current 25/25 lemma figure is single-judge and should not be cited as
   panel-grade.
6. **Compound-scoped Russian.** `marker-head` attributes a compound's whole gloss to its head
   lemma, so a bahuvrīhi like `vigata-BIr` "бесстрашный" lands on `BI` ("страх"). This is the
   wave-2 panel's systematic lemma defect #3, now extended to 1,018 more forms. The real fix is
   a compound layer, a design question for the segmenter wave.

## Revision history

| Date | Change | By |
|---|---|---|
| 20-07-2026 | Metadoc created; caveat + `√gam` reconciliation added to README (H1349 W1.4/W1.5). | Opus 4.8 (`claude-opus-4-8`) |
| 03-09-2026 | H3876: pending-republish note for the `marker-head` tier added to the README; backlog reconciled against what actually shipped (wave 2 measured, H3877 alternates UI done, cheda NO-GO) and two new items added. | Opus 5 (`claude-opus-5`) |

_Dr. Mārcis Gasūns_
