# Metadoc — ROOT_GLOSS_REGISTER_POLICY.md

_Created: 04-08-2026 · Last updated: 04-08-2026_

**Subject:** [ROOT_GLOSS_REGISTER_POLICY.md](https://github.com/gasyoun/SanskritRussian/blob/main/ROOT_GLOSS_REGISTER_POLICY.md)

- **Purpose:** the normative register standard for authored Russian citation glosses of
  Sanskrit verb roots — dictionary-neutral infinitives, with the explicit person/aspect/voice
  rule — ending per-batch local register decisions.
- **Audience:** gloss-batch authors (human or LLM), reviewers of curated gloss work, the UI
  headline-gloss layer.
- **Provenance:** H1860 (Fable 5, `claude-fable-5`), 04-08-2026. Inconsistency counts in §6
  measured directly over [root_glossary.tsv](https://github.com/gasyoun/SanskritRussian/blob/main/root_glossary.tsv)
  (105,058 rows; 1,205 verb roots) with a suffix-heuristic classifier (regexes documented in
  the §6 caveat; one-off script, not committed — repo is data-only by convention).
- **Limitations:** §6 class counts are heuristic (±a few %); the policy governs only the
  citation layer, not the generated corpus rollup; no conversion sweep of existing curated
  surfaces was performed (explicitly out of H1860 scope).
- **Improvement backlog (ranked):**
  1. ✅ Done 04-08-2026 (H2290) — conversion sweep of existing curated surfaces
     (SAMPLE_root_glossary.md ×2 copies, README √gam example, USE_CASES §1; index.html had no
     headline glosses — search placeholder + CTA only, kept).
  2. Replace the suffix-heuristic census with a morphology-parsed one (pymorphy3) if the ±few-%
     noise ever matters.
  3. Extend worked examples with media-tantum and defective-root cases as curated batches
     surface them.
- **Revision history:**
  - 04-08-2026 — created (H1860), policy adopted with 18 worked examples.
  - 04-08-2026 — H2290 conversion sweep of existing curated surfaces landed (backlog #1);
    policy text itself unchanged.

_Dr. Mārcis Gasūns_
