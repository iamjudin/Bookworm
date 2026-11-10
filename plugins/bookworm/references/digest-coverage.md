# Digest Coverage Gate

Use this gate for every book digest before vault handoff. It turns the existing
fullness promise into temporary, machine-checked workflow evidence. It does not
put diagnostic fields into the reader-facing note.

## Preserve the source inventory

Save the complete result of `inspect` as `source-inventory.json`. Every source
file or source section in that inventory must be assigned once to a coverage
group or explicitly excluded with a concrete reason. Cover pages, copyright,
navigation and duplicate front matter may be excluded.
Do not exclude a substantive chapter, worked exercise, appendix or case merely
to pass the gate.

For PDFs whose inspection has no section list, create an equivalent `sections`
array from the actual table of contents or page ranges. Each entry needs a
stable `id`, title and approximate `word_count`.

## Build coverage groups before drafting

A coverage group represents one reader job, usually one substantive chapter,
method stage or tightly connected source argument. It records the source files
that belong to it and the final note sections that carry its material. Several
substantive chapters may share a group only when they form one inseparable
argument and remain traceable through their source files.

For larger inventories, the gate requires a representative set of up to six
distinct groups across the substantive source. This prevents a whole book from
passing as one polished overview while still allowing pairs of tightly
connected chapters to share a reader-facing section.

For a batch, keep one inventory, ledger, note and gate result per book. Complete
the map, draft and gate for one book before finalizing the next. A passing book
must not hide a shallow result for another book.

## Separate verification from composition

The five dimensions are audit axes, not a reader-facing outline. Do not draft
every group as five paragraphs in the order mechanism, motivation, example,
limitation and application. Preserve the source's explanatory movement and
choose prose, lists or tables for the reader's actual task. One natural passage
may support several dimensions inside the same group.

Each group must carry at least three relevant dimensions and must include either
the central mechanism or a concrete application. Across the whole book, the
ledger must cover all five dimensions. Do not invent a limitation, example or
motivation merely to fill a slot that the source does not contain.

## Record reader evidence

Create `coverage-ledger.json` in the temporary run directory:

```json
{
  "schema": 1,
  "groups": [
    {
      "id": "chapter-01",
      "title": "Reader-facing group title",
      "source_files": ["OEBPS/Text/chapter01.xhtml"],
      "note_sections": ["Chapter 1 — Reader-facing heading"],
      "evidence": {
        "mechanism": ["Exact excerpt from the final note"],
        "motivation": ["Exact excerpt explaining why the step or idea exists"],
        "example": ["Exact excerpt containing a concrete case or worked example"],
        "limitation": ["Exact excerpt containing a failure mode, boundary or condition"],
        "application": ["Exact excerpt showing how a reader can use or test the idea"]
      }
    }
  ],
  "excluded": [
    {
      "source_file": "OEBPS/Text/cover.xhtml",
      "reason": "Cover page without substantive book content"
    }
  ],
  "visuals": [
    {
      "source_file": "OEBPS/Text/chapter01.xhtml",
      "source_image": "../Images/process.png",
      "decision": "included",
      "note_reference": "assets/book/chapter-01/process.png"
    },
    {
      "source_file": "OEBPS/Text/chapter01.xhtml",
      "source_image": "../Images/divider.png",
      "decision": "decorative",
      "reason": "Repeated ornamental chapter divider without reader meaning"
    }
  ],
  "questions": [
    {
      "question": "A concrete later-use question spanning this source group",
      "group_id": "chapter-01",
      "answer_evidence": [
        "Exact answer excerpt from the final note",
        "Exact limitation or application excerpt from the final note"
      ],
      "dimensions": ["mechanism", "limitation", "application"]
    }
  ]
}
```

Account for every image occurrence reported by the source inventory. Use
`included` for a meaning-bearing visual embedded or faithfully reconstructed in
the note. Use `decorative` only for a graphic without reader meaning and
`duplicate` only for an exact repeated visual. Both omission decisions require
a concrete reason. A visual that explains, compares, demonstrates or visualizes
an idea is meaning-bearing even when the surrounding prose also describes it.

Evidence excerpts must be exact, meaningful phrases from the named final note
sections. Do not use headings, generic boilerplate or the same sentence for
several groups. Reusing one passage for several dimensions inside its own group
is allowed when the passage genuinely performs those reading jobs. The ledger
records what the finished note already does. It must not dictate paragraph
count, paragraph order or visible labels in the note.

Ask enough concrete questions to span up to six different groups across the
beginning, middle and end of the source. Across the set, questions must test the
mechanism, motivation, example, limitation and application. A question is
answered only when the finished note contains the evidence, not when the model
can recall the source from its working context.

## Run the blocking audit

```bash
python3 scripts/bookworm_helper.py audit-digest-coverage \
  --inventory /path/to/run/source-inventory.json \
  --ledger /path/to/run/coverage-ledger.json \
  --note /path/to/run/final-note.md
```

The command fails when source items are unaccounted, too much source material
is excluded, a source visual is unaccounted or a meaning-bearing visual is absent
from the note, a coverage group has fewer than three relevant reading jobs or no
core mechanism/application, book-wide evidence misses a dimension, evidence is
absent from its named note section, or later-use questions do not span the book. Resolve a
failure by returning to the source and expanding or correcting the relevant
section. Do not add empty labels, weaken the inventory or move substantive
chapters into `excluded`.

Passing this gate proves accounting and local evidence presence. It does not
prove semantic accuracy, visual quality or source support. Keep the normal
reader review, figure review and source-grounding checks after it.
