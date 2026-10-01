---
name: deep-relational-notes
description: Generate structured, deep, connection-first study notes from a given topic or source text, using a fixed 9-section schema. Use whenever the user gives a topic name or pastes source material and asks for "notes" in this format.
---

# Deep Relational Notes — Generator Skill

## Purpose
Convert any topic name or source text into a single, deep, well-connected note
following a fixed schema. Optimized for a learner who:
- starts with a visual/relational mental model before formal detail
- wants ONE topic explored deeply rather than many topics covered shallowly
- needs both mathematical rigor (derivation) AND implementation (code) — not either/or
- maintains a Zettelkasten (linked, atomic notes), so every note must expose its links

## Hard rules (non-negotiable — read before generating anything)

1. **Source-boundedness.** If the user supplied source text (pasted text, uploaded file,
   image, PDF), every factual claim in the note MUST be traceable to that source. Do not
   add outside facts, dates, names, formulas, or claims not present in the source, even if
   you "know" them to be true from general knowledge. If elaboration beyond the source
   would help, put it in a clearly separate line prefixed `[beyond source]:` — never blend
   it into the source-derived content unmarked.

2. **No source = say so.** If the user gives only a topic name with no source text, you are
   generating from general knowledge. In that case, explicitly state at the top of the note:
   `Generated from general knowledge, no source text provided.` Do not silently invent a
   fake citation, page number, or textbook reference.

3. **DEFINITION section is conditional, not mandatory.** Only write a formal Definition if
   one is explicitly present in the source (word-for-word idea, not paraphrase-as-invention)
   or is an uncontested, standard textbook definition (general-knowledge mode). If no clean
   definition exists, write exactly: `No formal definition available in source.` Do not
   manufacture a definition to fill the slot.

4. **No fabricated numbers, quotes, or attributions.** Never invent a statistic, a named
   person's claim, a year, or a direct quote. If a specific number/date/name is needed but
   not confirmable from source or well-established general knowledge, write `[unconfirmed]`
   instead of guessing.

5. **Separate fact from inference explicitly.** Anywhere you are drawing a conclusion,
   connection, or analogy that is YOUR reasoning rather than a stated fact, prefix it with
   `(inference)`. This applies especially to the Context Map and Zettelkasten Links sections,
   where cross-topic links are often inferred, not stated in source.

6. **One topic per note.** Do not sprawl into adjacent topics beyond what's needed for
   Context Map / Links. Depth over breadth — this is the user's explicit preference.

7. **Code must be runnable, not pseudocode dressed up as code**, unless the topic is
   non-computational (pure philosophy/theory) — in that case, state
   `Not applicable — non-computational topic` in the Implementation section instead of
   forcing irrelevant code.

8. **If uncertain whether a claim is correct, flag it — do not smooth it over.**
   Use `(uncertain — verify)` inline rather than presenting a shaky claim with full confidence.

## Output schema (always exactly these 9 sections, in this order)

```
1. 🔗 CONTEXT MAP
   - Parent concept / field this topic belongs to
   - Prerequisite concepts (what must be understood first)
   - Downstream concepts (what this enables/leads to)
   - Mark inferred (not source-stated) links with (inference)

2. 🖼️ VISUAL/DIAGRAM
   - One diagram (or a clear text description of one if no diagram tool available)
     showing structure, flow, or relationships — not decoration
   - If truly no useful visual exists for this topic, state that explicitly instead
     of forcing one

3. 📖 DEFINITION
   - Formal definition IF present in source or standard in the field — else:
     "No formal definition available in source."
   - One concrete example illustrating the definition

4. 💡 CORE INTUITION (ELI5)
   - One plain-language analogy, no jargon
   - Analogy must be logically accurate to the mechanism, not just "sounds nice"

5. 📐 FORMAL DEPTH
   - Step-by-step derivation/proof/reasoning, each step justified (not just stated)
   - If a step relies on a prior result, name that result explicitly

6. 💻 IMPLEMENTATION
   - Runnable code (prefer pure/minimal dependencies) OR
   - "Not applicable — non-computational topic" if genuinely inapplicable

7. 🕸️ ZETTELKASTEN LINKS
   - [[related-note]] style backlinks
   - Note which parent/sibling notes this connects to
   - Mark inferred links with (inference)

8. ⭐ IMPORTANCE / RELEVANCE
   - Star rating (1–5) + one-line reason
   - If exam/course relevance is unknown, say "relevance unknown — no course context given"
     instead of guessing

9. ❓ OPEN QUESTIONS / GAPS
   - What remains unclear or unresolved from the source
   - If nothing is unclear, state "no open gaps identified" rather than inventing one
```

## Workflow when invoked

1. Check: did the user provide source text/file/image? → determines Rule 1 vs Rule 2 mode.
2. Check: is there a clean definition available? → determines Rule 3 behavior.
3. Generate all 9 sections in order, applying all Hard Rules above.
4. Do not add extra sections, headers, or commentary outside the 9-section structure
   unless the user asks a follow-up question separately.
5. If the topic is too broad for one note (e.g. "Machine Learning" as a whole), say so
   and ask the user to narrow it — do not silently shrink coverage without flagging it.

## Explicit non-goals
- This skill does not summarize entire chapters/books in one note — one atomic topic only.
- This skill does not produce motivational/filler language, summaries-of-summaries, or
  padding to make the note "look complete."
- This skill does not guess exam weightage, professor intent, or real-world statistics
  unless explicitly sourced.
