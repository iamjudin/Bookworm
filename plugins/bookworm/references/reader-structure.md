# Reader Structure Contract

Use this contract for every final Refine, Digest, and Enrich note.

## Choose the form by reading task

- Use compact Markdown tables for comparing options and for repeated short
  fields. Keep cells brief enough to scan at normal Obsidian note width.
- Use bullets for independent points and numbered steps for procedures or a
  sequence whose order changes the result.
- Use short connected paragraphs for causes, mechanisms, contradictions,
  trade-offs, uncertainty, and limitations.
- Move long explanations out of table cells. Adding a number before a dense
  paragraph does not make it readable.
- Keep one canonical detail layer. Do not present complete profiles in prose
  and repeat the same profiles in a table.
- Use Markdown tables. Convert reader-facing HTML tables before handoff.
- Treat an aligned data matrix inside a `text` or `plain` fence as
  reader-facing tabular data, not executable code. When its columns map
  unambiguously and its cells remain short, convert it to a Markdown table and
  preserve every header, value, unit, approximation sign, and note. Keep actual
  source code and exact quoted blocks unchanged.
- Do not turn every explanation into a table or every sentence into a bullet.

Before keeping repeated fields, choose one canonical representation:

1. When two or more entities share the same short fields and comparison is the
   reading task, use one matrix with entities as rows and fields as columns.
2. When the values need causal or multi-sentence explanation, use one section
   per entity with short labelled paragraphs. Do not append a separate
   `Parameter | Description` table that restates the same entity.
   Within that entity, do not state payments, channels, price, repeat value, or
   another field in an opening paragraph and then repeat it under bold field
   labels. Put each fact in the paragraph or the labelled field once.
3. Keep an experiment or procedure in one list or sequence. Do not split its
   hypothesis and observations into bullets while moving channel, budget, or
   intent into a second table.

During reader review, compare every table with the prose immediately before and
after it. Merge repeated facts into the chosen canonical layer while preserving
details that appear in only one source layer.

## Preserve meaning and evidence boundaries

Preserve numbers, units, negation, cumulative conditions, exceptions,
uncertainty, source proximity, and logical relationships. Structural editing
may change paragraph boundaries and list or table form. It must not silently
change what supports a claim, whether a condition is required, or whether an
exception limits the conclusion.

Code and exact quotations remain exact. In newly written reader-facing prose,
headings, lists, and tables, avoid semicolons. Rewrite the sentence or use a
full stop, comma, list, or short paragraph instead.

## Navigation and diagrams

Every table-of-contents entry must point to a real heading. Keep the first
screen useful for orientation without duplicating the detailed sections.

Treat Mermaid direction as an input to rendering, not proof of readability.
`TD` or `TB` can still produce a wide graph. Inspect the actual rendered width,
label wrapping, and horizontal scrolling when an Obsidian renderer is
available. If it is unavailable, record rendering as unverified and review node
count, label length, branching, and direction as limited evidence. Keep the
existing rule against silently splitting one diagram.

## Review sequence

Run deterministic cleanup first. Then perform an explicit semantic structure
pass. Finally read the note as a user would and run the structural audit helper.
Passing the helper does not prove semantic preservation or visual usability.
The reader review must still confirm that the conclusion is easy to find,
options are easy to compare, and the important exception remains visible.

```bash
python3 scripts/bookworm_helper.py audit-reader-structure /path/to/note.md
```

Review every reported issue. A semicolon inside fenced code or a Markdown
blockquote is preserved and excluded from the reader-text check. An exact
quotation in another form may be accepted after explicit review. Mermaid is
reported as render-unverified until it is inspected in an actual renderer.
Repeated generic two-column profile tables under one main section are reported
for review because they often hide a comparison or duplicate nearby prose.
An entity section that combines narrative prose with two or more unbulleted
bold fields is reported for review because it often repeats the same profile in
two forms. Experiment fields written as bullets remain one intentional list.
Aligned data left inside a `text` or `plain` fence is also reported for review
because Obsidian cannot scan or reflow it like a Markdown table.
