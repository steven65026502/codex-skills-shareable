---
name: design-system
description: Create or review design-token architecture and component specifications. Use for primitive-to-semantic-to-component tokens, CSS variables, spacing and typography scales, component states, and theme contracts. Do not use for general slide creation or one-off UI styling.
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
---

# Design System

Create a coherent token and component contract that can be implemented across themes and platforms. Keep project requirements and existing public APIs authoritative.

## Use when

- defining or migrating primitive, semantic, and component tokens;
- specifying component anatomy, variants, states, and accessibility behavior;
- mapping tokens into CSS variables or Tailwind configuration;
- reviewing hardcoded values, aliases, naming, or theme coverage.

Do not use for a one-off CSS change, general art direction, poster design, or slide authoring. Use `ui-styling` for shadcn/Tailwind component implementation and `slides` for a PPTX deliverable.

## Route to detail

- Token layers and naming: `references/token-architecture.md`
- Primitive values: `references/primitive-tokens.md`
- Semantic roles and themes: `references/semantic-tokens.md`
- Component tokens and specifications: `references/component-tokens.md`, `references/component-specs.md`
- States and variants: `references/states-and-variants.md`
- Tailwind mapping: `references/tailwind-integration.md`
- Preserved legacy material, including optional slide-token tooling: `references/full-guide.md`; read only when maintaining those existing assets.

## Workflow

1. Inspect the repository's existing tokens, component APIs, themes, and naming conventions.
2. Define the smallest missing layer. Prefer aliases over duplicated literal values.
3. Specify component states, contrast intent, and fallback behavior before generating code.
4. Update only the requested formats and consumers; do not introduce a parallel token source of truth.
5. Run available token validation, build, and targeted component checks.

## Completion and failure

Complete only when token references resolve, required themes and component states are represented, generated files parse or build, and the diff contains no unrelated hardcoded-value migration. If an existing token source or consumer mapping is ambiguous, preserve it, document the conflict, and stop before a breaking rename. Do not claim brand compliance or accessibility without the corresponding source and checks.
