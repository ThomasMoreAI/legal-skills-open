# Isolated relationship-edge resolver contract

Decide one candidate pair using only the two supplied canonical metadata
records. Do not inspect paths, filenames, other documents, or prior outputs.

Return `edge-resolver.schema.json` only. Use `linked` only when the receipts in
one record establish a supported relation to the other record. Set `src` to
the document whose receipt proves the relation, `dst` to the related document,
and copy that exact receipt as `quote`. Use `not-linked` when the records show
different instruments. Use `unresolved` when these two metadata records cannot
decide safely. For either non-linked decision, leave all edge fields null.

The resolver proposes an edge. It does not select a model, assemble families,
or make a lawyer-only confirmation.
