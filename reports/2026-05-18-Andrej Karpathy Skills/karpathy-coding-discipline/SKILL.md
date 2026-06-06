---
name: "karpathy-coding-discipline"
description: "Use when Codex writes, reviews, debugs, refactors, or edits code. Enforces careful assumptions, simple implementation, surgical changes, and verifiable success criteria to reduce common LLM coding mistakes."
metadata: {"openclaw":{"requires":{"anyBins":[]}}}
---

# Karpathy Coding Discipline

## Purpose

Use this skill whenever the user asks Codex to generate code, modify code, fix bugs, refactor, add tests, review a pull request, or explain implementation choices.

This skill biases Codex toward caution, minimal changes, and verifiable results. For trivial one-line tasks, keep the process lightweight but still preserve the same principles.

## Core Rules

### 1. Think before coding

Before editing or generating code:

- Identify the exact user request and the expected behavior.
- State important assumptions if the request is ambiguous.
- If multiple interpretations exist, choose the safest minimal interpretation and mention it.
- Do not silently add requirements that the user did not ask for.
- Push back when a simpler or safer approach exists.

### 2. Prefer simplicity

Implement the minimum code that satisfies the request.

- Do not add speculative features.
- Do not introduce unnecessary abstractions.
- Do not add new dependencies unless clearly justified.
- Do not add configurability for hypothetical future cases.
- If a small direct implementation works, prefer it over a framework-like design.

### 3. Make surgical changes

When editing an existing repository:

- Modify only the files and lines directly required by the task.
- Do not refactor unrelated code.
- Do not reformat unrelated files.
- Do not rename variables, functions, or files unless necessary for the task.
- Preserve the existing coding style, even if a different style is preferred.
- Remove only unused imports, variables, or functions created by the current change.
- If unrelated dead code or technical debt is found, mention it in the final summary instead of deleting it.

A useful check: every changed line should be traceable to the user's request.

### 4. Work toward verifiable success

Convert the request into a concrete success criterion.

Examples:

- "Fix this bug" -> reproduce the bug when feasible, then make the failing case pass.
- "Add validation" -> define invalid inputs, then add or update focused tests.
- "Refactor this module" -> preserve external behavior and run relevant tests before and after.
- "Improve performance" -> identify a measurable bottleneck or at least avoid changes that cannot be evaluated.

When possible:

- Run the smallest relevant test command.
- Add or update tests only when they directly support the task.
- If tests cannot be run, explain exactly why and describe the manual checks performed.

## Required Workflow

For non-trivial tasks, follow this compact workflow:

1. Inspect the relevant files before editing.
2. Form a minimal plan with clear success criteria.
3. Make the smallest necessary change.
4. Run or describe the most relevant verification.
5. Summarize changed files, verification results, and any remaining risks.

For very small tasks, do not over-explain; still keep the change minimal and focused.

## Output Style

When reporting back to the user:

- Start with the result, not a long process explanation.
- Mention the changed files.
- Mention tests or checks run.
- Mention unresolved assumptions or risks only if they matter.
- Do not claim tests passed unless they were actually run.

## Research Code Addendum

When working on research or experiment repositories:

- Do not change metric definitions unless explicitly requested.
- Do not change dataset paths, dataset formats, random seeds, or output schemas unless necessary.
- Preserve reproducibility.
- If a change may affect reported experimental results, clearly state that impact.
- Prefer minimal patches over broad cleanup.
