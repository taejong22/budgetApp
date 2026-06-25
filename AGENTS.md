# BudgetApp Project Rules

## Project Description
- Build and maintain a Python CLI budget app.
- The app uses CSV files as its primary data source and storage format.

## Coding Rules
- Use type hints on all public functions and methods.
- Keep every function at 50 lines or fewer.
- Prefer small, single-purpose helpers over large functions.

## TDD Rules
- Write tests before implementation.
- Red, green, refactor is mandatory for every new behavior.

## Quality Rules
- Keep cyclomatic complexity at 10 or below.
- Refactor early if a function or module starts to drift above the threshold.

## Quality Check Rules
- Before committing, always ask the `qa_engineer` sub-agent to review quality.
- Do not skip the QA pass, even for small changes.

## Test Commands
- Run tests with `pytest`.
- Check complexity with `radon cc`.

## Commit Rules
- Commit once a single feature is complete.
- Push after the feature commit is ready.
