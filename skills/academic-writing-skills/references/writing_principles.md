# Writing Principles

Universal rules for rigorous academic writing. Use paper-specific overrides in
`.paper/style_overrides.md` when a journal, advisor, or field convention differs.

## 1. Structure And Logic

### 1.1 Findings First

State the result before the figure citation or mechanism.

Correct:

> Adaptation reduces renter flood damage by 19%. Relocation to lower-exposure
> tracts accumulates over time, so damage avoidance contributes a growing share
> of the reduction.

Wrong:

> Figure 5 shows that renters relocate to safer tracts, which reduces damage by
> 19%.

Why: readers scan for the finding. Opening with "Figure X shows" hides the
scientific point.

### 1.2 Mechanism For Every Result

Every result needs a mechanism sentence. A complete result paragraph usually has:

```text
finding -> mechanism -> implication for the research question
```

If the reader can still ask "why?" after the finding, the paragraph is not done.

### 1.3 Sentence-To-Sentence Continuity

Each sentence must connect to the previous one through a clear pivot,
demonstrative, noun repeat, or causal link. If sentence B could be moved
elsewhere without changing meaning, the paragraph is probably a list, not an
argument.

### 1.4 Complete The Local Explanation

Do not defer an explanation to a later section when the current paragraph needs
it. A section may point forward, but it should not make the reader wait to
understand the current result.

### 1.5 Subsection Openings

Open each subsection with one sentence that states what the subsection does and
why it is needed at this point in the paper.

### 1.6 Hypothesis-Driven Research Questions

When possible, place a directional expectation before each research question:

```text
We expect X because Y, given Z.
```

Descriptive research questions without a directional expectation often produce
weak Results sections.

## 2. Precision

### 2.1 No Overclaim

Match certainty to evidence.

Direct language is appropriate for:

- established empirical facts,
- mathematical definitions,
- method settings controlled by the authors.

Hedged language is required for:

- patterns inferred from data,
- simulation output,
- statistical associations,
- mechanisms not directly observed.

Prefer "is consistent with", "suggests", "appears to", "is associated with",
"may explain", or "contributes to" when evidence is inferential.

### 2.2 No Vague Intensifiers

Words such as "substantial", "major", "dramatic", "strong", and "large" need a
number or comparison. Delete them if they cannot be quantified.

"Significant" is valid only when reporting a statistical test with a p-value,
confidence interval, or equivalent inferential result.

### 2.3 Precise Targets

Replace vague nouns with the actual quantity:

- "the distribution declines" -> "the median household loss declines"
- "the gap widens" -> "the homeowner-renter damage gap widens"
- "various factors" -> name the factors

Demonstratives such as "this", "these", and "that" need clear antecedents.

### 2.4 Panel-Level Figure Citations

Use panel-specific citations when panels exist:

- "Figure 5b, blue line"
- "Figure 6e, tail region"

Avoid bare "Figure 5" when the claim depends on one panel.

### 2.5 Numbers Must Match Source Output

Re-check numbers after every revision. Abstract numbers, Results numbers, code
output, tables, and figure annotations drift during editing.

### 2.6 Numbers Must Be Visible Or Traceable

Any precise number in prose must be visible on a figure, in a table, in code
output, or in a cited source. If the reader cannot verify it, either add the
evidence or soften the prose.

### 2.7 Symbols Must Match

Notation in prose, equations, legends, and figures must match exactly. Do not
reuse one symbol for distinct quantities.

## 3. Mechanism And Argument

### 3.1 Counterintuitive Result Audit

Before writing a surprising result, run this audit:

1. Denominator check: verify what the percentage is divided by.
2. Direction plausibility: trace the causal chain through the method or theory.
3. Subgroup magnitude check: compare the subgroup to related groups.
4. Artifact check: test initialization, censoring, measurement, model, or coding
   artifacts.
5. Absolute-value sanity check: compare against prior literature or real-world
   ranges.

Report the audit before treating the result as a contribution.

### 3.2 Mechanisms Need Evidence — And A Section

Mechanism explanations in Results should point to either:

- a visible quantity in another figure or table,
- a method rule already described,
- a cited theory or empirical finding.

**Length rule.** Results mechanism = one (rarely two) sentence that names the
cause and points to the evidence. Anything longer — multi-result synthesis,
theory tie-in, comparison with prior literature, or speculative explanation —
belongs in Discussion §3 (Mechanism synthesis).

**Failure mode to avoid.** A Results paragraph that reads like Discussion
(3-4 sentences of mechanism narrative without pointing to a figure or
method rule). This blurs the boundary and forces the reader to re-read in
Discussion. Conversely, a Discussion paragraph that only restates Results
numbers without adding mechanism or implication is also a failure — it
duplicates rather than synthesises.

**Runnable check.** For each Results paragraph, after writing:
1. Is the finding stated first?
2. Is there exactly one mechanism sentence?
3. Does that sentence point to a figure / table / method rule / citation?

If any answer is no, revise. If the mechanism needs more than one sentence,
move the additional content to Discussion.

### 3.3 Causal Claim Audit

Before writing a causal claim, check each of the following. For each threat,
write down a one-sentence reason it is or is not ruled out. If it cannot be
ruled out, hedge the claim accordingly.

| Threat | Question | Hedge if not ruled out |
|---|---|---|
| Correlation vs. causation | Could the same data pattern arise without a causal link? | "is associated with" |
| Reverse causality | Could Y cause X instead of X causing Y? | "co-varies with" |
| Confounding / omitted variable | Is there a Z that could explain both X and Y? | "is associated with, controlling for [vars]" |
| Selection bias | Is the sample non-random with respect to the outcome? | "Among [sample], …" + state generalisability limit |
| Base-rate neglect | Did you compare the rate to the population base rate? | Report both rates explicitly |
| Survivorship bias | Are dropouts / failures excluded from the denominator? | State the denominator and inclusion criteria |
| Ecological fallacy | Are you inferring individual behaviour from group means? | Use "at the [group] level, …" |
| Regression to the mean | Was the sample chosen on an extreme value? | Compare to a matched non-extreme control |
| Immortal time bias | (Survival contexts) Is some follow-up period unobservable by design? | Realign exposure-time accounting |
| Collider bias | Did you condition on a variable affected by both X and Y? | Do not condition; or report unconditional estimate |
- faithful treatment of prior work.

If the study design cannot support causality, use associational language.

### 3.4 Contribution Test

Before claiming a contribution, ask:

```text
Could a knowledgeable reader guess this without running the study?
```

If yes, it is background or common sense. If no, it may be a contribution.

## 4. Word Choice

### 4.1 Avoid GPT-Style Vocabulary

Audit new prose with `banned_words.md`.

### 4.2 Avoid Awkward Agency

Variables do not "receive" values, data do not "know" things, and models do not
"discover" unless that is technically accurate. Use plain verbs that name the
actor and action.

### 4.3 Causal Connectors

Avoid oral connectors such as "because" and "so" when formal alternatives are
available:

- "Given that X, Y..."
- "As X increases, Y..."
- "X increases, resulting in Y."
- "This pattern reflects..."
- "This difference arises from..."

### 4.4 Limit Colons And Semicolons

Both punctuation marks are commonly over-used in academic prose. They splice
independent clauses (semicolon) or set up a definition / list (colon) when
two separate sentences would read more cleanly.

Guideline: at most one semicolon and one colon per paragraph in body prose.
Citation lists `(Author, year; Author, year)`, abbreviation lists `(WSA = H
or VH; ACA = H or VH)`, ratio notations, and equation-introducing colons
inside parentheses do not count toward the cap.

Common replacements:

- Prose colon list ("Three factors: (a)..."): integrate into grammar
  ("Three factors — A, B, and C — contributed", noting the em-dash style
  caveat in §4.7) or split into separate sentences with a numbered breakout.
- Colon at sentence end ("X: Y is the case"): use a period and let Y stand
  as its own sentence.
- Mid-sentence semicolon between two independent clauses: prefer two
  sentences. Use semicolon only when the two clauses are short, tightly
  parallel, and a period would feel choppy.
- Semicolon as a list separator with already-comma-rich items: acceptable;
  this is the one case the rule does not apply.

The Yang-group convention is stricter (≤1 semicolon per paragraph); other
journals are more permissive. Apply the stricter form by default — it
forces clearer sentence boundaries and reads less like LLM-generated prose,
which tends to over-use both marks.

### 4.5 Polish After Structure

Do not polish before the logic is fixed. The normal order is:

1. claim structure,
2. mechanism accuracy,
3. evidence consistency,
4. word choice,
5. transitions and rhythm.

### 4.6 Domain-Native Vocabulary

Match terminology to the field the paper is being submitted to. Reviewers
scan for their field's native vocabulary, and jargon imported from a
different sub-field, a software repository, a method paper, or an adjacent
discipline signals "this author is not from our discipline" before the
science is even read. Vocabulary drift is common when:

- a manuscript began in one field and was refocused for another (a
  computational draft refocused for ecology; a method paper refocused for
  clinical readers; a basic-science draft refocused for a translational
  audience),
- a paper integrates text from a software repository, technical report, or
  internal documentation whose audience differs from the target journal,
- a co-author from a neighbouring discipline contributes prose using their
  own field's vocabulary,
- a model description was originally written for a methods journal and is
  now part of an applied paper.

Before settling on a noun or verb, check:

1. Would a senior reviewer in the target field use this exact word in their
   own paper?
2. If the word originated in a different field (CS, statistics, engineering,
   pharmacology, ML, software documentation, qualitative social science,
   etc.), is there a target-field equivalent the reviewer would prefer?
3. Has a novel term that names the paper's contribution been defined inline
   with a target-field concrete example at first use?

What counts as "field-foreign" is defined by the target audience, not by
the source field. The same word may be perfectly native in one journal and
read as jargon in another:

| Term | Native in | Foreign in (without redefinition) |
|---|---|---|
| "validator", "pipeline", "stack" | software engineering, CS | water resources, ecology, clinical medicine |
| "RL policy", "reward function" | reinforcement learning, robotics | epidemiology, materials science |
| "loss function", "regularisation" | machine learning, statistics | applied biology, qualitative social science |
| "p-hacking", "garden of forking paths" | statistical methodology | engineering design, computational physics |
| "harm reduction", "PrEP" | public health, epidemiology | basic pharmacology, materials chemistry |
| "ablation study" | machine learning | clinical trials, field ecology |
| "ground truth" | computer vision, ML | qualitative research, history of science |

The fix is not to delete the concept — it usually carries technical content
that belongs in the paper — but to rewrite the surrounding sentence in the
target field's native vocabulary. Per-paper vocabulary swaps belong in
`.paper/style_overrides.md` under a "Domain Vocabulary Swaps" section,
where the manuscript records its own field-foreign-to-field-native
substitution table. `banned_words.md` covers field-agnostic GPT-style
vocabulary; field-foreign jargon is whatever the target reviewer pool
does not use, and is therefore paper-specific.

Novel terms that name the paper's contribution are allowed even when they
have no native equivalent, but they must be defined inline at first use
with a concrete example in the target field's terms.

Apply this audit after structure and mechanism are correct, alongside the
banned-word audit in `banned_words.md`.

### 4.7 No Invented Compound Terms

Use existing field vocabulary. Do not invent noun-noun (or noun-noun-noun)
compounds by joining words with hyphens to label a concept the paper is
introducing. Compound nouns coined ad hoc read as software-API names, not
as scientific concepts, and they signal to reviewers that the author is
labelling rather than explaining.

Warning signs of invented compounds:

- Two or more nouns joined by hyphens to name a thing the paper proposes
  ("validator-stack", "computational-interior", "theoretical-mobility",
  "cognitive-coordinates", "rule-engine", "decision-pipeline").
- A compound with no recent literature precedent in the target field
  (quick check: search the term in Google Scholar or in the journal's
  recent issues; if there are zero hits in the target field, it is
  invented).
- A compound that reads as a category name in a software repository
  rather than as a phrase a domain expert would use.

When the paper needs to name a concept, prefer in this order:

1. An existing single noun used in the target field.
2. A short noun phrase using prepositions ("the layer of institutional
   rule checks", "switching the underlying behavioural assumption",
   "the agent's own reported appraisal").
3. A defined-term abbreviation introduced once with a plain-language
   gloss ("the Irrational Behaviour Rate, IBR, defined as the fraction
   of decisions in which the agent's stated appraisal contradicts its
   proposed action").

Hyphenated compounds ARE appropriate in three settings:

- Adjectival modifiers before a noun ("water-rights system", "agent-based
  model", "self-reported appraisal", "field-foreign vocabulary"). These
  modify a downstream noun and are standard English.
- Standard scientific compounds with literature precedent ("cross-sectional",
  "open-access", "risk-perception", "decision-making", "agent-based").
- Quoted technical names from a software repository or cited paper, used
  to identify rather than to coin a concept.

The rule applies to ad hoc invention. If unsure, default to a plain noun
phrase: a phrase with prepositions is almost always more readable than a
chained-noun compound.

Apply this audit at the same time as §4.6 (domain-native vocabulary) —
invented compounds and field-foreign terms tend to appear together when
text is imported from a software or method draft.

## 5. Voice, Tense, And Rhythm

### 5.1 Active And Passive Voice

Use active voice for claims and contributions. Use passive voice when the actor
is conventional or irrelevant. Do not enforce either as a universal rule.

### 5.2 Tense

- Past tense: methods performed and specific results.
- Present tense: definitions, equations, stable facts, and paper structure.
- Present perfect: literature background when framing a gap.

### 5.3 Sentence Length

Avoid monotonous sentence rhythm. Target an average near 20-30 words and revise
sentences above 45 words unless the journal style or content justifies them.

### 5.4 Repetition

Repeated nouns, verbs, and adjectives can be useful for precision, but repeated
phrasing across consecutive sentences often reads machine-generated. Keep
defined technical terms stable while varying nontechnical wording.

## 6. Figures

Use `figure_conventions.md` for detailed checks. Core rules:

- Same concept -> same label, color, and annotation style.
- Precise numbers in prose must be visible or traceable.
- Captions should be self-contained.
- Panel citations should be specific.
- Field-standard plots are preferred over invented plot types.

## 7. Redundancy

Do not define the same term repeatedly across sections. Do not restate Methods
inside Results unless the interpretation requires a specific equation, rule, or
parameter.

## 8. Revision Process

### 8.1 Base Revisions On The Accepted Version

When revising against advisor or reviewer comments, start from the accepted
manuscript version and change only what the comments require.

### 8.2 Anchor Every Comment

Before answering a comment, identify the exact sentence, paragraph, figure, or
table it targets. Do not guess.

### 8.3 Build Scripts Are Source Of Truth

If a compiled manuscript and source scripts disagree, trust the build scripts or
source files, then regenerate the manuscript.

### 8.4 Iterative Rewrite Reality

Heavy rewrites usually need separate passes:

1. structure,
2. mechanism,
3. terminology,
4. evidence consistency,
5. academic polish,
6. word count.

Set this expectation before trying to fix everything in one pass.
