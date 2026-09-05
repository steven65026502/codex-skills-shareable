# Research workspace manifest schema

Use this local contract for files written under a project's `.research/` directory. Unknown values stay empty; do not infer research questions, hypotheses, dataset licenses, or experiment results.

## `project_manifest.yml`

Required top-level keys:

```yaml
project_name: ""
research_area: ""
research_question: ""
current_stage: discovery
last_updated: "YYYY-MM-DD"
main_entrypoints: []
datasets: []
evidence_artifacts: []
```

`current_stage` must be one of:

- `discovery`
- `exploration`
- `experiments`
- `writing`
- `rebuttal`
- `submission`

Paths are project-relative strings. A missing path must not be represented as if it exists.

## `experiment_matrix.yml`

Use a list under `experiments`. Each record needs a stable `id`, a `status`, and empty-safe description fields:

```yaml
experiments:
  - id: exp-001
    status: planned
    hypothesis: ""
    method: ""
    entrypoint: ""
    inputs: []
    outputs: []
    evidence: []
```

Allowed statuses are `planned`, `running`, `complete`, `blocked`, and `abandoned`. Do not mark an experiment complete without an observable output or evidence reference.

## `data_dictionary.yml`

Use a list under `datasets`:

```yaml
datasets:
  - id: data-001
    path: ""
    description: ""
    format: ""
    schema: []
    provenance: ""
    license: ""
    sensitive: null
```

Use `null` when sensitivity, provenance, or license is unknown; add the uncertainty to `open_questions.md`.

## Supporting Markdown files

- `run_log.md`: append the date, inspected sources, written files, validation result, and unresolved limitations.
- `decisions.md`: record only decisions evidenced by project material or the user.
- `open_questions.md`: record missing or ambiguous facts; it is not a backlog of invented work.

## Validation

Parse YAML using a UTF-8-aware parser. Check required keys, enum values, unique IDs, and referenced paths. Existing human-authored non-empty values win unless the user explicitly requests regeneration. A failed refresh must leave the previous valid file recoverable.
