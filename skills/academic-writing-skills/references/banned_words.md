# Banned Words, Phrases, And Patterns

Items below should be deleted, replaced, quantified, or justified. Paper-specific
overrides in `.paper/style_overrides.md` take precedence.

This file covers field-agnostic GPT-style vocabulary. For field-foreign
jargon that signals "this author is not from our discipline" to reviewers
(terminology imported from a sub-field, method paper, software repository,
or neighbouring discipline that the target journal's reviewer pool does
not use natively), see `writing_principles.md` §4.6 and the "Domain
Vocabulary Swaps" section of `.paper/style_overrides.md`.

For noun-noun hyphenated compounds invented to label a concept the paper
introduces (rather than drawn from existing field vocabulary) and for the
limit on semicolons and colons in body prose, see `writing_principles.md`
§4.7 and §4.4 respectively.

## 1. Single Words

### Verbs

| Avoid | Prefer |
|---|---|
| delve | examine, investigate |
| utilize | use |
| leverage | use, apply, draw on |
| harness | use |
| navigate | address, handle |
| foster | encourage, produce |
| showcase | show, present |
| underscore | show, emphasize sparingly |
| bolster | support, strengthen |
| garner | receive, gather |
| embark | begin |
| unpack | explain, examine |
| endeavor | aim, work |
| elucidate | show, explain |
| substantiate | support |
| facilitate | enable, allow, or rewrite |
| exemplify | show, illustrate |

### Adjectives

Delete or quantify: crucial, pivotal, intricate, meticulous, vibrant, robust,
nuanced, multifaceted, comprehensive, paramount, imperative, indispensable,
noteworthy, novel, innovative, holistic, seamless, substantial, substantive,
major, dramatic.

"Significant" is allowed for statistical significance. It is not allowed as a
generic intensifier.

### Adverbs

Usually delete: undeniably, remarkably, notably, crucially, importantly,
ultimately, meticulously, markedly, substantially, considerably.

Also delete when used as fillers (not when carrying technical content such as
*statistically significantly* or *spatially explicitly*): essentially,
fundamentally, inherently, particularly, specifically, effectively, largely,
broadly, generally, relatively (without a comparator), arguably.

### Redundant Qualifiers

Delete the qualifier — the noun already carries the meaning:

| Redundant | Use |
|---|---|
| completely unique | unique |
| absolutely essential | essential |
| totally novel | novel (and quantify why) |
| fully comprehensive | comprehensive (and quantify) |
| extremely critical | critical (and justify) |
| deeply concerning | concerning (and state the consequence) |
| highly significant | significant (with statistical evidence) |
| very important | (delete; if it matters, the sentence will show why) |

### Metaphorical Nouns

Avoid: tapestry, landscape as a metaphor, beacon, realm, interplay, synergy,
testament, paradigm, cornerstone.

## 2. Banned Phrases

- "It is important to note that..."
- "It is worth noting that..."
- "In recent years..."
- "In today's world..."
- "plays a crucial role"
- "provides a comprehensive framework"
- "as mentioned above"
- "as established earlier"
- "beyond this"
- "in this regard"
- "with respect to this"
- "sheds light on"
- "a testament to"
- "the interplay between"
- "ever-evolving"
- "at the forefront"
- "moving forward"

## 2a. AI-Conclusion And Throat-Clearing Phrasings

These are among the most reliable LLM-prose tells in 2025-2026. They add
no information and signal AI-generated wrap-up rhetoric. Delete or rewrite.

| Avoid | Prefer |
|---|---|
| in conclusion, / to conclude, | (delete — the sentence itself should be the conclusion) |
| in summary, / to summarise, | (delete or use a structured roadmap heading) |
| as discussed above / as we have seen / as established earlier | (delete; if needed, cite §X) |
| having explored / having considered | (delete or rewrite as a direct claim) |
| with that said / having said that / that being said | however, (or rewrite) |
| to that end / in light of this | (delete or name the specific reason) |
| the field of X has witnessed / has seen rapid growth | quantify: "publications grew from N to M, 20YY-20YY" |
| in the rapidly evolving landscape of X | (delete; usually meaningless) |
| paving the way for | "supports", "motivates", "suggests" |
| shedding light on | "shows", "indicates", "reveals" |
| this study aims to / sets out to / seeks to / endeavours to | "we test whether", "we estimate", "we show" |
| at the heart of / lies at the core of | "central to" (and only when justified) |

## 3. Weak Demonstratives

Flag subject-less openings such as:

- "This ensures..."
- "This enables..."
- "This allows..."

Replace "this" with the actual antecedent unless the previous sentence makes it
unmistakable.

## 4. Sentence Starters

Generally avoid:

- "Furthermore,"
- "Moreover,"
- "Additionally,"
- "Building on..."
- "Together,"
- repeated "By [verb]-ing, we..."

Style-dependent starters such as "Although", "Yet", "By contrast", "Therefore",
and "Thus" should follow journal and advisor preferences.

## 5. Structural Patterns

### Long Dash Overuse

Some journals allow long dashes and some advisors dislike them. The universal
rule is overuse: more than two long dashes in one paragraph usually signals
sloppy or AI-like prose. Follow `.paper/style_overrides.md`.

### Adjective Stacks

Avoid noun piles such as "comprehensive robust multi-scale framework". Use one
adjective and a precise phrase.

### Colon Lists Inside Prose

Avoid "Three factors: (a)...". Integrate the list into the sentence or use a
proper list.

### Repetitive Openings

Three consecutive sentences beginning with "The" or "This" should be revised
unless the repetition is deliberate and clear.

### Participial Chains

Avoid paragraph openings such as "Building..., integrating..., and leveraging...".
Use direct claims.

## 6. Overclaim Language

For inferred findings, avoid:

| Avoid | Prefer |
|---|---|
| confirms | is consistent with |
| proves | suggests |
| demonstrates | indicates |
| determines | shapes |
| controls | influences |
| ensures | tends to |
| eliminates | reduces |
| drives | contributes to |
| explains | may explain, is consistent with |

Use "significant" only with statistical evidence.

## 7. Mechanistic Trigger Phrases

These phrases often invite reviewer pushback unless the method explicitly
supports them:

| Trigger phrase | Safer replacement |
|---|---|
| preferentially selected | more likely to |
| systematic bias | average difference of X |
| filter tightens | share changes from A to B |
| removed from the denominator | no longer included in the group |
| residual group | remaining group meeting criterion X |
| isolates the effect | focuses on, conditions on |
| hard-coded | specified in Methods |
| explains away | accounts for X of the gap |
| must, necessarily, invariably | tends to, on average, in N cases |

## 8. Detection Heuristic

For any suspicious sentence, ask:

1. Would a domain-expert PhD student write this?
2. Does removing the sentence lose information?
3. Are there too many adjectives before one noun?
4. Does the sentence use a metaphor where a technical term is needed?
5. Does every demonstrative have a clear antecedent?
