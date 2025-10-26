# uv demo | Python DevOps practices

<!--TODO:
[ ] review the whole guide
[ ] GitHub workflow status, move details to below only short description.
[ ] Add table for code quality standards
[ ] GitHub repo config
-->

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![TestPyPI](https://img.shields.io/badge/TestPyPI-latest-blue)](https://test.pypi.org/project/uv-demo/) [![Coverage](https://codecov.io/gh/ac-willeke/uv-demo/branch/main/graph/badge.svg)](https://codecov.io/gh/ac-willeke/uv-demo) [![Safety](https://img.shields.io/badge/Safety-Dashboard-blue)](https://platform.safetycli.com/codebases/uv-demo/findings)

A demo repository showcasing Python project development and packaging best practices using [uv](https://docs.astral.sh/uv/getting-started/installation/). This project demonstrates project structure, dependency management, containerization with Docker and automated code quality, security scanning and deployment workflows using GitHub Actions (GHA).

**Table of Contents**

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Documentation](#documentation)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Project Overview

This repository serves as a demonstration and learning resource. To use this as a template for new projects, refer to the [setup guide](./docs/setup-guide.md) in the documentation.

### Key Features
<!-- List key features and capabilities -->

- **Python packaging**:
  - Dependency management with uv
  - Automated versioning using setuptools-scm
- **GHA** workflows for CI/CD and security:
  - Code quality checks with pre-commit, ruff, mypy, and pytest
  - Security scans with Safety, CodeQL, Dependabot, and Zizmor
  - Python package deployment to Test PyPI
  - Container image deployment to GitHub Container Registry
- **Developer tools**: VS Code integration, development containers, Taskfile automation

### Repository Structure
<!-- Directory layout -->

- `.github/workflows` - GHA for CI/CD pipelines, security scanning and dependency updates (see [GitHub Actions Workflows](#github-actions-workflows)).
- `pyproject.toml` - Python package config, dependencies, and build settings
- `Taskfile.yml` - Automated tasks for setting up the dev environment, running code quality checks and more. Run `task help` to see all available tasks or refer to the [Command Cheatsheet](./docs/command-cheatsheet.md).

Full overview of the repository structure is available in the [Repository Structure](./docs/repo-structure.md) documentation.

### Workflow Statuses

| Job | Status | Description |
|---|---|---|
| **CI Python** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/ci-python.yml?branch=main&label=&style=flat) | Code quality checks, testing, coverage |
| **CD Python** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/cd-python.yml?label=&style=flat) | Package deployment to Test PyPI |
| **CI Docker** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/ci-docker.yml?branch=main&label=&style=flat) | Build and test Docker image |
| **CD Docker** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/cd-docker.yml?label=&style=flat) | Container deployment to GitHub Registry |
| **Security Scan - Safety** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-safety.yml?branch=main&label=&style=flat) | Python dependency vulnerability scanning |
| **Security Scan - CodeQL** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-codeql.yml?branch=main&label=&style=flat) | Python and GHA security analysis |
| **Security Scan - Zizmor** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-zizmor.yml?branch=main&label=&style=flat) | GHA workflow security scan |
| **Dependabot** |  | Automated dependency updates |

Results of the security scans are visible in the [Security](https://github.com/ac-willeke/uv-demo/security/code-scanning) tab of the GitHub repository.

## Getting Started
<!-- For end users -->

The **uv-demo** package is a minimal package with a single function that prints the package name. You can install this package from [Test PyPI](https://test.pypi.org/project/uv-demo/) or pull the containerized version from [GHCR](https://github.com/ac-willeke/uv-demo/pkgs/container/uv-demo). The main purpose of this repository is to explore development tools and observe the CI/CD pipeline in action. To get started, follow the steps in the [Development Workflow](#development-workflow) section.

### Installation

> [!NOTE]
> This package is published to Test PyPI for demonstration purposes. Test PyPI is a testing environment for package deployment without affecting the official PyPI index. If you're using this repo to test out your own deployment pipeline, make sure not to publish test versions to the official PyPI index.


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

3. **Automatic setup**: The devcontainer automatically:
   - Configures VS Code with recommended settings and extensions per [devcontainer.json](.devcontainer/devcontainer.json)
   - Installs development tools: [Git](https://git-scm.com/), [uv](https://docs.astral.sh/uv/), [pre-commit](https://pre-commit.com/), [Task](https://taskfile.dev/installation/)
   - Sets up the Python environment with dependencies in `.venv` via `task dev-setup`, which runs `uv sync --dev` and executes code quality checks and test coverage

4. **Test the installation with Task commands**:

    Task is used to automate common development tasks *(see [Taskfile.yml](Taskfile.yml))*.

   ```bash
   # Test the package
   task run
   # or
   uv run uv-demo

   # Run quality checks
   task check

   # Run local CI workflow
   task ci-local

   # Clean up
   task clean
   ```

5. **Test the notebook**: Open `notebooks/demo.ipynb` and select the `.venv` kernel. If you have problems activating the `.venv` refer to the [setup guide](./docs/setup-guide.md).

6. **Configure the GitHub Repository**: If you fork this repository or use it to create your a new repository from scratch, you'll need to configure your GitHub repository to connect with **Test PyPI**, **Safety** and **Code Coverage**. Also, verify that your **security scans** are properly set up. See the **GitHub Repository Configuration** section in the [setup guide](./docs/setup-guide.md) for instructions.

## Development Workflow

### Code Quality Standards

Follow PEP8, use type hints, and include docstrings in reStructuredText format. All quality checks are automated through Task commands, pre-commit hooks and CI workflows.

See the [Code Quality and Security Standards](./docs/code-and-security-standards.md) guide to see which rules are enforced in this repo.

### GHA Workflows

The repository includes automated workflows for code quality, security, and deployment:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| **CI Python** | `push`, `pull_request` to `main` | Code quality checks, testing, coverage |
| **CD Python** | `push` to `main` with version tags | Package deployment to Test PyPI |
| **CD Docker** | `push` to `main` with version tags | Container deployment to GitHub Registry |
| **Safety Scan** | `push`, `pull_request`, `schedule` | Python dependency vulnerability scanning |
| **CodeQL Analysis** | `push`, `pull_request`, `schedule` | Code security analysis |
| **Zizmor Security** | `push`, `pull_request` | GHA workflow security |



The demo workflows can be customized or removed based on your specific project requirements. At minimum, I recommend including the **CI Python** workflow for code quality and testing, as well as the Security workflows: **CodeQL**, **Safety**, and **Zizmor**.

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

For more commands see: [Command Cheatsheet](./docs/command-cheatsheet.md)

### Branch Protection

The `main` branch is protected with the following rules:
- Require pull request reviews before merging
- Require status checks to pass before merging
- Require branches to be up to date before merging

## Documentation
<!-- Links to docs, API references, guides, troubleshooting tips -->

## Acknowledgements

This project incorporates best practices from the Python and DevOps communities, including:

- Astral-sh's [uv Documentation](https://docs.astral.sh/uv/) and Docker configuration example [astral-sh/uv-docker-example](https://github.com/astral-sh/uv-docker-example)
- Eric Riddoch's [Taking Python to Production](https://www.udemy.com/course/setting-up-the-linux-terminal-for-software-development/) course
- Marvelous MLOps [MLOps with Databricks](https://www.youtube.com/results?search_query=marvelous+mlops) course


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
