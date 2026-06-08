# Contributing Guidelines

Welcome to the **noaa-temp-analyzer** repository! To maintain a clean project, please follow these workflow and style guidelines.

---

## Project Stack & Setup

We use **uv** for environment and dependency management.

### Project Stack

* **Python:** 3.10
* **Core Tools:**

  * `pandas`
  * `matplotlib`
  * `click` (CLI)
  * `logging`
  * `ruff` (linting)
  * `pytest` (testing)

### Local Environment Setup

Run the following command to set up your local development environment:

```bash
uv sync
```

---

## GitLab Workflow & Branching

We mostly use **GitLab** as our primary communication platform, however we might still use other platforms.

### General Rules

* Do **not** commit directly to the `main` branch.
* Create a separate GitLab issue for each task before starting work.
* Create a dedicated branch linked to the corresponding issue.
* Let one other person review before merging
* Document important decisions in issues or merge requests

### Branch Naming Conventions

Example branch names;

```text
feature/cli
feature/data-loading
feature/temperature-analysis
docs/readme
test/parser-tests
ci/pipeline
```

---

## MR & Review

### Requirements

1. Push your branch to GitLab.
2. Open a Merge Request (MR).
3. Document important decisions in the related issue or MR description.
4. Obtain approval from at least one other team member before merging into `main`.

---

## Commit Message Style

To keep the Git history clean and readable, use the following commit message prefixes:

| Prefix      | Purpose                                     |
| ----------- | ------------------------------------------- |
| `feat:`     | New functionality                           |
| `fix:`      | Bug fixes                                   |
| `docs:`     | Documentation changes                       |
| `test:`     | Tests                                       |
| `ci:`       | CI/CD changes                               |
| `chore:`    | Setup and configuration                     |
| `refactor:` | Code restructuring without behavior changes |

### Examples

```text
feat: add NOAA data parser
fix: handle missing temperature values
docs: update installation instructions
test: add parser unit tests
refactor: simplify data loading logic
```

---

## Code Testing

Before opening a Merge Request.

### Linting

```bash
ruff check .
```

### Testing

```bash
pytest
```

### Requirements

* All linting checks must pass.
* All tests must pass successfully.
* New functionality should include appropriate tests whenever possible.

---

### Updating These Guidelines

These guidelines reflect the team's decisions. As the project evolves, this document may be modified.
