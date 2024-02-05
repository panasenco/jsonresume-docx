# Developing jsonresume_docx

## Setup

### VS Code Dev Containers / GitHub Codespaces

In VS Code, reopen the project in a devcontainer.
Alternatively, open GitHub Codespaces.
Your project should be automatically installed.

### Just pip

```
pip install -e .[dev]
```

## Formatting and linting

We use [ruff](https://docs.astral.sh/ruff/) for formatting and linting Python code.

### Formatting

```
ruff format jsonresume_docx/
```

### linting

List errors:

```
ruff check jsonresume_docx/
```

Auto-fix errors:

```
ruff check --fix jsonresume_docx/
```