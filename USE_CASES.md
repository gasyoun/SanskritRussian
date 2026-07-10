# Use cases — Sanskrit → Russian glossary

_Created: 01-07-2026 · Last updated: 01-07-2026_

What the three-layer glossary ([root](https://github.com/gasyoun/SanskritRussian/blob/main/root_glossary.tsv)
· [lemma](https://github.com/gasyoun/SanskritRussian/blob/main/lemma_glossary.tsv) ·
[surface](https://github.com/gasyoun/SanskritRussian/blob/main/surface_glossary.tsv)) is good for.
Everything below is answerable from the committed data or the
[live search page](https://gasyoun.github.io/SanskritRussian/).

## 1. Bilingual lexicography — draft a Sa→Ru dictionary entry
Look up a root and get its **full ranked set of Russian equivalents** across every attested
form and prefixed verb. `√gam` → пришел (196) · отправился (177) · ушел (141) · достигает (99)
· явился (92) … (678 forms, 44 lemmas, 7,116 occurrences). The frequency ranking gives the
lead gloss and the long tail in one view — the skeleton of a dictionary sense list.

## 2. Reverse lookup — Russian word → its Sanskrit sources
On the [live page](https://gasyoun.github.io/SanskritRussian/) toggle **"search Russian"** and
type e.g. `идти` — see every root/lemma that was ever rendered by that Russian word. Useful for
translators checking how a Russian term maps back onto Sanskrit vocabulary.

## 3. Translation-memory / MT seed
The flat TSVs (`key → ru → count`) are a ready **Sa→Ru phrase table**: 190,838 surface forms
and their attested Russian renderings with frequencies. Drop-in seed for a translation memory,
an alignment prior, or few-shot examples for an LLM translating Sanskrit into Russian.

## 4. Polysemy & translation-variance metrics
`n_forms` and the length of each `translations` list quantify **how varied** a root's Russian
rendering is. Compare a semantically tight root (few glosses) against a broad one (`√gam` /
`√kf`) — a corpus-grounded polysemy signal for DH / computational lexicology.

## 5. Register-aware vocabulary study
Every record carries a `registers` breakdown (Ṛgveda, Atharvaveda, epic, …). Ask *how a root's
Russian rendering shifts by layer of the language* — e.g. Vedic vs epic senses of the same root.

## 6. Learner-facing "semantic range" cards
For teaching: show a student the spread of real Russian equivalents a root takes across attested
texts, instead of a single dictionary gloss — grounded in 1.09M aligned tokens, not intuition.

## 7. Morphological-coverage / gap analysis
The [failure typology](https://github.com/gasyoun/SanskritRussian/blob/main/README.md#failure-typology-78842-unresolved-forms--140667-tokens)
+ [`surface_unresolved.tsv`](https://github.com/gasyoun/SanskritRussian/blob/main/surface_unresolved.tsv)
expose exactly which forms DCS + Vidyut could **not** lemmatize (rare simplex, long compound,
proper name). A worklist for improving Sanskrit lemmatizers, and a benchmark of their ceiling
(87.1 % of tokens resolved).

## What it is **not**
Not a hand-checked dictionary: Russian glosses are corpus translations (some contextual,
occasional errors), roots are attached by an automated DCS/Vidyut join (homographs attributed to
the dominant lemma). Treat frequencies as evidence, not ground truth — see the
[method + typology](https://github.com/gasyoun/SanskritRussian/blob/main/README.md).

_Dr. Mārcis Gasūns_
