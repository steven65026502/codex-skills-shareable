# Claim-Evidence Audit

Use this reference before writing or revising Abstract, Results, Discussion,
Conclusion, cover letter, and reviewer response. These sections often compress
claims and are therefore prone to overclaim.

## Goal

Every claim should map to evidence and an allowed certainty level.

```text
claim -> evidence -> certainty -> revision
```

## Evidence Types

| Evidence type | Examples | Typical allowed language |
|---|---|---|
| Direct measurement | observed data, lab measurement, survey response | shows, estimates, reports |
| Statistical inference | regression, test, confidence interval | is associated with, suggests |
| Simulation output | ABM, scenario run, model ensemble | suggests, is consistent with |
| Mechanistic rule | method specification, equation, algorithm | follows from, is specified by |
| Literature | cited peer-reviewed result | prior work reports, prior work suggests |
| Expert judgment | advisor note, domain convention | treat as assumption unless cited |

## Audit Table

Use this table when auditing:

```markdown
| Claim | Location | Evidence Source | Certainty Allowed | Problem | Revision |
|---|---|---|---|---|---|
| ... | Abstract sentence 4 | Figure 5b | suggests | "proves" overclaims | replace with "suggests" |
```

## Required Checks

- [ ] The claim has a visible or cited evidence source.
- [ ] The certainty matches the evidence type.
- [ ] The number in the claim matches the source.
- [ ] The source is current, not an old draft or stale run.
- [ ] The mechanism is either observed, specified in Methods, or framed as an
      interpretation.
- [ ] The same claim is worded consistently across Abstract, Results,
      Discussion, Conclusion, and cover letter.

## Disposition When A Claim Cannot Be Verified

If the audit cannot find a source for a claim, do NOT leave it as-is. Choose
one of five dispositions:

| Option | When to use | Example |
|---|---|---|
| 1. Drop | The claim is not load-bearing for the contribution. | A throwaway adjective in Discussion; a parenthetical aside. |
| 2. Hedge | The claim is plausible but evidence is inferential. | "X reduces Y by Z%" → "X may reduce Y" or "X is associated with a reduction in Y". |
| 3. Move to Discussion | The claim is interpretation, not result. | A mechanism narrative misplaced in Results. |
| 4. Add a Limitations caveat | The claim is needed but evidence is partial or indirect. | "We cannot directly observe Z; this finding assumes…". |
| 5. Add the evidence | The evidence exists but is missing from the figure/table/text. | Re-run the analysis or add an SI panel; cite the existing source. |

**Never leave a precise number unverified.** If none of (1)-(5) is possible,
remove the number and rewrite the sentence qualitatively. A vague number is
worse than no number; a reviewer will check the number.

**Record dispositions in the audit table.** Add a "Disposition" column (1-5)
so future audits can verify each previously unverifiable claim was actually
handled and not silently retained.

## Certainty Rules

Use direct verbs only when the study design supports them:

- "we set", "we define", "the model computes" for design choices,
- "the table reports" for displayed values,
- "the regression estimates" for model output.

Use hedged verbs for inferred findings:

- "suggests",
- "is consistent with",
- "appears to",
- "is associated with",
- "may explain",
- "contributes to".

Avoid:

- proves,
- confirms,
- demonstrates, unless the design truly demonstrates,
- ensures,
- eliminates,
- conclusively shows.

## Abstract And Conclusion Gate

Before finalizing Abstract or Conclusion:

1. Extract each claim sentence.
2. Map each claim to a source.
3. Remove claims without evidence.
4. Reduce certainty where evidence is inferential.
5. Verify all numbers against current Results or figures.

## Reviewer Response Gate

When a reviewer challenges a claim:

1. Identify the exact sentence.
2. Locate the evidence source.
3. Decide whether the claim should be defended, hedged, moved, or deleted.
4. Record the manuscript change in the response table.
