# Reader Structure Validation

## Scope

This validation covers the shared reader structure rules for Bookworm Digest,
Refine, and Enrich. It checks where the behavior is defined, applied, and
verified. It does not install or publish a new plugin version and it does not
write fixtures into a user vault.

## Behavior map

| Concern | Definition | Application | Verification |
| --- | --- | --- | --- |
| Shared reading forms | `plugins/bookworm/references/reader-structure.md` | All three skill workflows load the contract before editing or composing | Contract tests and the read-only structure audit |
| Meaning versus paragraph shape | Refine core promise | Refine semantic structure pass after deterministic cleanup | Bidirectional proposition review and the Refine fixture |
| Section coverage and later questions | Digest fullness contract | Drafting from the source section or argument map | Six questions across mechanism, motivation, example, limitation, condition, and source |
| Useful additions | Enrich scope rules | Each addition closes a recorded gap and keeps a labelled source boundary | Temporary source ledger and the Enrich fixture |
| Navigation and dense structures | Shared contract | Reader review before handoff | HTML, long cell, heading target, semicolon, and Mermaid audit findings |

## Bounded fixtures

The fixtures are public and synthetic except for the Enrich source, which uses
the public RFC 2606 specification. They contain no private vault content.

### Refine before

The input places timing, cost, a prohibition, two cumulative conditions, a
causal explanation, uncertainty, and a nearby source link in one dense
paragraph. It also contains an HTML table, mismatched heading links, an exact
quotation, code, and a wide-risk top-to-bottom Mermaid graph.

### Refine after

The output uses one compact Markdown comparison table. It moves causal details
into short paragraphs and exposes the cumulative conditions as bullets. The
exact quotation and code remain unchanged. The expected note retains `12 ms`,
`18 ms`, both costs, the prohibition, both required conditions, the 40-run
sample, the provisional status, and the source link.

### Digest result

The source map has five substantive sections. The expected note retains the
mechanism, why each step exists, the 40-run example, failure conditions, the
cumulative application condition, uncertainty, and the source anchor. Six
questions can be answered from the finished note without returning to the
source.

### Enrich result

The original note names reserved example domains but does not explain why they
are reserved. One labelled addition explains the reservation mechanism and the
conflict it prevents. The gap and contribution category stay in the temporary
ledger instead of appearing as technical labels in the reader note.

## Test record

| Check | Result |
| --- | --- |
| Focused reader structure and contract tests | 98 passed, 4 dependency-based skips under system Python |
| Complete Bookworm test suite with the bundled workspace Python | 105 passed with no skips in 0.748 seconds |
| Public package validator | Passed |
| Git whitespace validation | Passed |
| Skill Creator quick validator | Not run because its PyYAML dependency is absent from both available Python runtimes |
| Obsidian fixture rendering | Unverified |

The exact interactive Codex model variant and reasoning effort are not exposed
to the repository process, so they cannot be recorded reliably. The executable
checks use Python `unittest` and no model. The run was isolated to repository
fixtures and temporary files under `/private/tmp`. No Brain note, installed
plugin cache, marketplace record, tag, or remote branch was changed.

## Remaining limits

- The structure audit detects mechanical risks. It cannot prove that every
  source proposition survived or that every final claim is supported.
- Long table detection uses a conservative character and sentence heuristic.
  Borderline cells still need reader judgment.
- Blockquotes are treated as exact quotations for the semicolon check. Inline
  quotations require explicit review when they contain a semicolon.
- Mermaid direction, edge count, and line length do not establish rendered
  width. The fixtures were not registered as a temporary Obsidian vault and
  were not copied into Brain, so horizontal scrolling remains unverified.
- Package installation and public release require separate authorization.
