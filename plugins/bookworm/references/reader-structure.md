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
- Do not turn every explanation into a table or every sentence into a bullet.

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
