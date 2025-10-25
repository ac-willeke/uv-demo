# uv demo | Python DevOps practices

<!--TODO:
[ ] review the whole guide
[ ] GitHub workflow status, move details to below only short description.
[ ] Add table for code quality standards
[ ] GitHub repo config
-->

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![TestPyPI](https://img.shields.io/badge/TestPyPI-latest-blue)](https://test.pypi.org/project/uv-demo/) [![Coverage](https://codecov.io/gh/ac-willeke/uv-demo/branch/main/graph/badge.svg)](https://codecov.io/gh/ac-willeke/uv-demo) [![Safety](https://img.shields.io/badge/Safety-Dashboard-blue)](https://platform.safetycli.com/codebases/uv-demo/findings)

A demo repository showcasing Python project development and packaging best practices using UV. This project demonstrates project structure, dependency management, containerization with Docker and automated code quality, security scanning and deployment workflows using GitHub Actions.

**Table of Contents**

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Documentation](#documentation)
- [License \& Acknowledgements](#license--acknowledgements)

## Project Overview

This repository serves as a demonstration and learning resource. To use this as a template for new projects, refer to the [setup guide](./docs/setup-guide.md) in the documentation.

### Key Features
<!-- List key features and capabilities -->

- **Python packaging**:
  - Dependency management with UV
  - Automated versioning using setuptools-scm
- **GitHub Actions** workflows for CI/CD and security:
  - Code quality checks with pre-commit, ruff, mypy, and pytest
  - Security scans with Safety, CodeQL, Dependabot, and Zizmor
  - Python package deployment to Test PyPI
  - Container image deployment to GitHub Container Registry
- **Developer tools**: VS Code integration, development containers, Taskfile automation

### Repository Structure
<!-- Directory layout -->

- `.github/workflows` - Github Actions for CI/CD pipelines, security scanning and dependency updates. See the [Development Workflow](#Development Workflow) section to learn more about these GHA workflows.
- `pyproject.toml` - Python package config, dependencies, and build settings
- `Taskfile.yml` - Automated tasks for setting up the dev environment, running code quality checks and more. Run `task help` to see all available tasks or refer to the [Command Cheatsheet](./docs/command-cheatsheet.md).

Full overview of the repository structure is available in the [Repository Structure](./docs/repo-structure.md) documentation.

### Workflow Statuses

| Job | Status | Description |
|---|---|---|
| **CI Python** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/ci-python.yml?branch=main&label=&style=flat) | • Pre-commit hooks (ruff, mypy, etc.)<br>• Test coverage with pytest and codecov<br>• Python dependency analysis<br>• Build and test package |
| **CD Python** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/cd-python.yml?label=&style=flat) | • Build Python package (wheel + sdist)<br>• Publish to Test PyPI<br>• Triggered by git tags or manually in GitHub |
| **CI Docker** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/ci-docker.yml?branch=main&label=&style=flat) | • Build and test Docker image |
| **CD Docker** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/cd-docker.yml?label=&style=flat) | • Build and push Docker image<br>• Publish to GitHub Container Registry<br>• Triggered by git tags or manually in GitHub |
| **Safety Scan** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-safety.yml?branch=main&label=&style=flat) | • Python dependency scan<br>• Results in GitHub Actions log and on the [Safety](https://platform.safetycli.com/codebases/uv-demo/findings) dashboard |
| **CodeQL Analysis** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-codeql.yml?branch=main&label=&style=flat) | • Python and GitHub Actions security analysis<br>• Results in [Security](https://github.com/ac-willeke/uv-demo/security/code-scanning) tab |
| **Zizmor Security** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-zizmor.yml?branch=main&label=&style=flat) | • GitHub Actions security scan<br>• Results in [Security](https://github.com/ac-willeke/uv-demo/security/code-scanning) tab |
| **Dependabot** |  | • Automated dependency updates<br>• Security vulnerability alerts<br>• Configured via `.github/dependabot.yml` |


The demo workflows can be customized or removed based on your specific project requirements. At minimum, I recommend including the **CI Python** workflow for code quality and testing, as well as the Security workflows: **CodeQL**, **Safety**, and **Zizmor**. See the [Development Workflow](#Development Workflow) section to learn more about these GHA workflows.

## Getting Started
<!-- For end users -->

The **uv-demo** package is an empty package with a single function that prints the package name. You can install this package from Test PyPI or pull the containerized version.

But the value of this repository lies in learning the development tools and seeing the CI/CD pipeline in action. So I recommend following the [Development](#development) section to learn these steps.

### Installation

> [!NOTE]
> This package is published to Test PyPI for demonstration purposes. Test PyPI serves as a testing environment for package deployment without affecting the official PyPI index. Do not publish demo packages to the official PyPI index.


Install the demo package from Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ uv-demo
```

```python
import uv_demo
uv_demo.main()
# > Hello from uv-demo!
# > Version: 0.0.1
```

Or pull and run the container:

```bash
docker pull ghcr.io/ac-willeke/uv-demo:latest

docker run --rm ghcr.io/ac-willeke/uv-demo:latest
# > Hello from uv-demo!
# > Version: 0.0.1
```


## Development Setup
<!-- For contributors -->

> [!TIP]
> **Recommended Setup:** Use [GitHub Codespaces](https://github.com/features/codespaces) or [VS Code Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) for a consistent environment. Local OS setup without containers requires extra configuration.

The following steps configure your development environment using VS Code Dev Containers. For local setup without containers, refer to the [setup guide](./docs/setup-guide.md) in the documentation.

### Prerequisites
<!-- Software versions, system requirements, dependencies, account requirements (APIs, services) -->

- [Docker](https://docs.docker.com/engine/install/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
extension

### Setup
<!-- Step-by-step installation guide -->

1. **Open the project**: Clone and open the project folder in VS Code or use [GitHub Codespaces](https://docs.github.com/en/codespaces).

2. **Start the devcontainer**: When prompted, reopen the folder in the Devcontainer. If not prompted, manually trigger it via the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select "Dev Containers: Reopen in Container".

3. **Automatic setup**: The devcontainer will configure:
   - VS Code settings and extensions
   - Development tools: Task, uv, pre-commit
   - Python environment with dependencies

4. **Test the installation**:
   ```bash
   # Test the package
   task run
   # or
   uv run uv-demo

   # Run quality checks
   task check

   # Run local CI workflow
   task ci-local
   ```

5. **Explore the demo**: Open `notebooks/demo.ipynb` and select the `.venv` kernel, then follow the [Quick Start Guide](./docs/demo-quickstart.md).

### Environment Variables
<!-- List of necessary environment variables
- variable names
- descriptions
- default values (if any)
-->

### Development Tools installed in the Container

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Git](https://git-scm.com/)
- [Pre-commit](https://pre-commit.com/)
- [Task](https://taskfile.dev/installation/)

## Development Workflow

### Code Quality Standards

Follow PEP8, use type hints, and include docstrings in reStructuredText format. All quality checks are automated through pre-commit hooks and CI workflows.

### GitHub Actions Workflows

The repository includes automated workflows for code quality, security, and deployment:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| **CI Python** | `push`, `pull_request` to `main` | Code quality checks, testing, coverage |
| **CD Python** | `push` to `main` with version tags | Package deployment to Test PyPI |
| **CD Docker** | `push` to `main` with version tags | Container deployment to GitHub Registry |
| **Safety Scan** | `push`, `pull_request`, `schedule` | Python dependency vulnerability scanning |
| **CodeQL Analysis** | `push`, `pull_request`, `schedule` | Code security analysis |
| **Zizmor Security** | `push`, `pull_request` | GitHub Actions workflow security |

### Local Development Commands

Use these commands for local development and testing:

```bash
# Setup and quality checks
task install          # Install dependencies and setup environment
task check            # Run all quality checks
task ci-local         # Simulate CI pipeline locally

# Testing and running
task test             # Run test suite
task run              # Run the demo package
task run-docker       # Run in Docker container

# Code formatting and security
task format           # Format code with ruff
task security         # Run security scans
```

### Branch Protection

The `main` branch is protected with the following rules:
- Require pull request reviews before merging
- Require status checks to pass before merging
- Require branches to be up to date before merging

## Documentation
<!-- Links to docs, API references, guides, troubleshooting tips -->

## License & Acknowledgements
<!-- License info, inspirations, related projects -->

This project is licensed under the [MIT License](LICENSE) and incorporates best practices from the Python and DevOps communities, including:

- Astral-sh's [uvDocumentation](https://docs.astral.sh/uv/) and Docker configuration example [astral-sh/uv-docker-example](https://github.com/astral-sh/uv-docker-example)
- Eric Riddoch's [Taking Python to Production](https://www.udemy.com/course/setting-up-the-linux-terminal-for-software-development/) course
- Marvelous MLOps [MLOps with Databricks](https://www.youtube.com/results?search_query=marvelous+mlops) course

---
