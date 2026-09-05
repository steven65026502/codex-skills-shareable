---
name: ui-styling
description: Implement accessible application UI with shadcn/ui, Radix UI, and Tailwind CSS. Use for responsive layouts, forms, dialogs, tables, menus, component states, theme integration, and dark mode in a codebase using those tools. Do not use for posters, general art direction, or design-token architecture.
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
---

# UI Styling

Implement application interfaces with the repository's existing shadcn/ui, Radix, and Tailwind conventions. Reuse installed components and tokens before adding custom primitives.

## Use when

- building or repairing forms, dialogs, menus, tables, navigation, or responsive layouts;
- adding keyboard, focus, error, loading, disabled, and empty states;
- applying an existing theme or dark mode through Tailwind variables;
- adapting shadcn/Radix components without breaking their accessibility behavior.

Do not use for posters, canvas art, broad visual direction, or token architecture. Use `frontend-skill` for art direction and `design-system` for token contracts.

## Route to detail

- Component selection and composition: `references/shadcn-components.md`
- Accessibility behavior: `references/shadcn-accessibility.md`
- Theme integration: `references/shadcn-theming.md`
- Tailwind utilities and customization: `references/tailwind-utilities.md`, `references/tailwind-customization.md`
- Responsive behavior: `references/tailwind-responsive.md`
- Preserved canvas and legacy workflow details: `references/canvas-design-system.md`, `references/full-guide.md`; read only for an explicitly relevant existing asset.

## Workflow

1. Inspect the framework, Tailwind configuration, installed component registry, and existing design tokens.
2. Choose the nearest existing accessible component and preserve its semantics.
3. Implement the smallest requested change, including interaction states and responsive behavior.
4. Avoid unnecessary dependencies, arbitrary values, and duplicate component abstractions.
5. Run the project's tests plus targeted keyboard, focus, viewport, and contrast checks as applicable.

## Completion and failure

Complete when the requested interface works at the relevant viewports, keyboard and focus flows remain usable, state variants are visible, and project checks pass. If the expected shadcn/Radix/Tailwind setup or component is absent, report the mismatch and either use the repository's actual stack or request approval before adding a dependency. Do not claim accessibility from component choice alone.
