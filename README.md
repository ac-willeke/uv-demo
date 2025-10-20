# UV demo - Python DevOps practices

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![TestPyPI](https://img.shields.io/badge/TestPyPI-latest-blue)](https://test.pypi.org/project/uv-demo/) [![Coverage](https://codecov.io/gh/ac-willeke/uv-demo/branch/main/graph/badge.svg)](https://codecov.io/gh/ac-willeke/uv-demo) [![Safety](https://img.shields.io/badge/Safety-Dashboard-blue)](https://platform.safetycli.com/codebases/uv-demo/findings)

A demo repository showcasing Python project development and packaging best practices using UV. This project demonstrates project structure, dependency management, containerization with Docker and automated code quality, security scanning and deployment workflows using GitHub Actions.

**Features:**

- **Python Tools**: uv for dependency management, setuptools-scm for dynamic versioning.
- **GitHub Actions** workflows for **CI/CD** pipelines including:
    - **Code Quality** with pre-commit, ruff, mypy, and pytest.
    - **Security scanning** with Safety, CodeQL, Dependabot, and Zizmor.
    - **Python** deployment to Test PyPI.
    - **Container** deployment to GitHub Container Registry (ghcr.io).
- **Developer Tools**: Development containers, VS Code integration, and task automation.

## Workflow Statuses

| Job | Status | Description |
|---|---|---|
| **CI Python** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/ci-python.yml?branch=main&label=&style=flat) | • Pre-commit hooks (ruff, mypy, etc.)<br>• Test coverage with pytest and codecov<br>• Python dependency analysis<br>• Build and test package |
| **CD Python** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/cd-python.yml?label=&style=flat) | • Build Python package (wheel + sdist)<br>• Publish to Test PyPI<br>• Triggered by git tags or manually in GitHub |
| **Safety Scan** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-safety.yml?branch=main&label=&style=flat) | • Python dependency scan<br>• Results in GitHub Actions log and on the [Safety](https://platform.safetycli.com/codebases/uv-demo/findings) dashboard |
| **CodeQL Analysis** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-codeql.yml?branch=main&label=&style=flat) | • Python and GitHub Actions security analysis<br>• Results in [Security](https://github.com/ac-willeke/uv-demo/security/code-scanning) tab |
| **Zizmor Security** | ![Status](https://img.shields.io/github/actions/workflow/status/ac-willeke/uv-demo/scan-zizmor.yml?branch=main&label=&style=flat) | • GitHub Actions security scan<br>• Results in [Security](https://github.com/ac-willeke/uv-demo/security/code-scanning) tab |

The demo workflows can be customized or removed based on your specific project requirements. At minimum, we recommend including the **CI Python** workflow for code quality and testing, as well as the Security workflows: **CodeQL**, **Safety**, and **Zizmor**.

## Quick Start

### Prerequisites

- [uv](https://docs.astral.sh/uv/installation/)
- [Git](https://git-scm.com/), [GitHub](https://github.com/) account, and [GitHub CLI](https://cli.github.com/)
- [Task](https://taskfile.dev/installation/)
- [Docker](https://docs.docker.com/engine/install/) (optional)
- [VS Code](https://code.visualstudio.com/) (optional)

### Setup

Task is used to automate common development tasks *(see [Taskfile.yml](Taskfile.yml))*. To set up the project without Task, you can follow the instructions in the [Installation Guide](docs/installation.md).

```bash
# Clone the repository
gh repo clone ac-willeke/uv-demo
cd uv-demo

# Development setup (installs dependencies, hooks, runs checks)
task dev-setup

# Test the application
task run
# → "Hello from uv-demo!"
# → "Version: xxxx"

# See all available commands
task --list
```

## Development Workflow

To contribute to the project or start your own project based on this demo, follow the steps below:

1. **Setup**:
   - Follow the setup instructions above or refer to the [Installation Guide](docs/installation.md).
   - Follow the demo walkthrough in the [Quick Start Guide](docs/demo-quickstart.md).
2. **Develop**:
    - Create a branch for your feature or bug fix: `feat/<name>` or `fix/<name>`.
    - Make your changes.
    - Ensure code meets the quality standards by running `task check`.
3. **Integrate**:
    - Check that all CI tests pass locally with `task ci-local`.
    - Push your branch to GitHub.
    - Create a pull request against the `main` branch.
    - Await review and merge; your branch will be automatically deleted after merging.
    - Clean up local git:
        - enable pruning: `git config --global fetch.prune true`
        - delete merged branch locally: `git branch -d <branch-name>`
4. **Deploy**:
    - Create a git tag for releases (e.g., `v0.0.1`) using `task tag`.
    - Create a PR from `release/<version>` to `main` to deploy the new release.
    - Once merged to `main`, the CD workflows are triggered:
        - CD Python automatically builds and publishes the package to Test PyPI.
        - CD Docker builds and pushes the container image to GitHub Container Registry.

### Key Commands

```bash
task check            # Run all quality checks (ruff, mypy, pytest, deptry)
task format lint-fix  # Format and lint code with ruff
task security         # Run security scans (Safety, Zizmor)
task build            # Build Python package
task tag              # Prepare a new release (create git tag)
```

For a complete command reference, see [Command Cheatsheet](docs/command-cheatsheet.md).

## Documentation

Documentation is available in the [`docs/`](docs/) directory:

### Getting Started

- **[Installation](docs/installation.md)** - Step-by-step setup guide
- **[Quick Start](docs/demo-quickstart.md)** - Get up and running quickly with Taskfile

### Development
- **[Development Guide](docs/development.md)** - Complete development workflow and tools

### CI/CD
- **[Workflows](docs/ci-cd/workflows.md)** - GitHub Actions CI/CD pipelines
- **[Deployment](docs/ci-cd/deployment.md)** - Package building and publishing

### Reference
- **[Command Cheatsheet](docs/command-cheatsheet.md)** - All commands organized by tool
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions

## Acknowledgements

This project incorporates best practices from the Python and DevOps communities, including:
- Astral-sh's [UV Documentation](https://docs.astral.sh/uv/) and Docker configuration example [astral-sh/uv-docker-example](https://github.com/astral-sh/uv-docker-example)
- Eric Riddoch's [Taking Python to Production](https://www.udemy.com/course/setting-up-the-linux-terminal-for-software-development/) course
- Marvelous MLOps [MLOps with Databricks](https://www.youtube.com/results?search_query=marvelous+mlops) course


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
