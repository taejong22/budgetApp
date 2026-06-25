---
name: budget-app-cli
description: Python CLI budget app workflow for CSV-based transaction handling, TDD implementation, and quality review. Use when working in this repository on budgeting features, CSV parsing/loading, transaction logic, tests, complexity checks, or QA review before commit.
---

# Budget App CLI

## Scope
- Work on the Python CLI budget app in this repository.
- Treat CSV files as the system of record.

## Workflow
1. Write or update tests before implementation.
2. Keep functions small and typed.
3. Prefer focused helpers for CSV parsing, transaction logic, and summaries.
4. Verify complexity and test coverage before commit.
5. Route the change through `qa_engineer` review before committing.

## Constraints
- Use type hints on public functions and methods.
- Keep functions at 50 lines or fewer.
- Keep cyclomatic complexity at 10 or below.

## Validation
- Run `pytest`.
- Run `radon cc`.

## Commit Habit
- Commit each finished feature as its own change.
- Push after the feature commit is ready.
