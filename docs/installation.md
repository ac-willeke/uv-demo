# Installation Guide

This guide will walk you through setting up the **uv-demo** project on your local machine. Ensure you meet the prerequisites and choose the method that best fits your workflow.

- [Prerequisites](#prerequisites)
- [Method 1: Taskfile setup](#method-1-taskfile-setup)
- [Method 2: Manual setup with uv](#method-2-manual-setup-with-uv)
- [Method 3: Devcontainer setup with VS Code](#method-3-devcontainer-setup-with-vs-code)
- [VS Code Integration](#vs-code-integration)
- [Getting Help](#getting-help)

## Prerequisites

#### Tools

- [uv](https://docs.astral.sh/uv/installation/)
- [Git](https://git-scm.com/), [GitHub](https://github.com/) account, and [GitHub CLI](https://cli.github.com/)
- [Task](https://taskfile.dev/installation/) (necessary for method 1 - Taskfile setup)
- [Docker](https://docs.docker.com/engine/install/) (necessary for method 3 - Devcontainer setup)
- [VS Code](https://code.visualstudio.com/) (necessary for method 3 - Devcontainer setup)

#### Clone the Repository

```bash
# Clone from GitHub
gh repo clone ac-willeke/uv-demo
cd uv-demo

# Alternative: using git directly
git clone https://github.com/ac-willeke/uv-demo.git
cd uv-demo
```

## Method 1: Taskfile setup

If you have [Task](https://taskfile.dev/installation/) installed:

1. Set up the Python environment using Task commands.

    ```bash
    # Development setup
    task dev-setup

    # See all available commands
    task --list
    ```

    The `dev-setup` task will:
    - Install Python dependencies with uv
    - Set up pre-commit hooks
    - Run initial code quality checks
    - Install the package in development mode

2. Test the installation:

    ```bash
    # Test the package
    task run
    # → "Hello from uv-demo!"
    # → "Version: xxxx"
    ```

3. Follow the Demo instructions in the [Quick Start Guide](./demo-quickstart.md) to explore development commands and the Jupyter notebook.

4. (Optional) Configure VS Code: [see VS Code Integration](#vs-code-integration).


## Method 2: Manual setup with uv

If you prefer a local setup without using Devcontainers or Task, follow these steps:

1. Set up the uv environment from the `pyproject.toml` and `uv.lock` files.

    ```bash
    # Navigate to your cloned repository
    cd uv-demo

    # Create .venv with dev dependencies
    uv sync --dev
    ```

2. Test the installation:

    ```bash
    # Run the main CLI command
    uv run uv-demo
    # → "Hello from uv-demo!"
    # → "Version: xxxx"
    ```

3. Follow the Demo instructions in the [Quick Start Guide](./demo-quickstart.md) to explore development commands and the Jupyter notebook.

4. (Optional) Configure VS Code for development: [see VS Code Integration](#vs-code-integration).

## Method 3: Devcontainer setup with VS Code

If you have [Docker](https://docs.docker.com/engine/install/) and [VS Code](https://code.visualstudio.com/) installed:

1. Open the project folder in VS Code or [GitHub Codespaces](https://docs.github.com/en/codespaces).
2. When prompted, reopen the folder in the Devcontainer. If not prompted, you can manually trigger it via the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select "Dev Containers: Reopen in Container".
3. The Devcontainer will automatically:
   - Configure the recommended VS Code settings and extensions
   - Install the recommended dev tools: Task, uv, pre-commit, etc.
   - Set up the uv environment
4. Test the installation:
   - Test the package: `task run` or `uv run uv-demo`
   - Run quality checks: `task check` or individual commands
   - Run the example notebook: Open `notebooks/demo.ipynb` and select the `.venv` kernel.
5. Follow the Demo instructions in the [Quick Start Guide](./demo-quickstart.md) to explore development commands and the Jupyter notebook.


## VS Code Integration

The project includes VS Code configuration for optimal development experience:

1. **Extensions**: Install recommended extensions from `.vscode/extensions.json` (VS Code will prompt you).
2. **Settings**: Code formatting, linting, and type checking are pre-configured in `.vscode/settings.json` and should be automatically detected. If not, check your workspace/folder settings.
3. **Python Environment**: VS Code should automatically detect the `.venv` created by uv.


### Manual Python Environment Selection

The Python extension and Jupyter Notebooks extension detect the `.venv` created by `uv` package manager as the default environment. If not, set the enviroment manually:

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
2. Type "Python: Select Interpreter"
3. Choose the interpreter in `./.venv/bin/python` (Linux/macOS) or `.\.venv\Scripts\python.exe` (Windows)

### Terminal Environment

To activate the virtual environment in your terminal:

```bash
# Activate the virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Verify activation (should show the project's Python)
which python
python --version
```

### Jupyter Notebook Setup

To use the project package in Jupyter notebooks:

1. Open the demo notebook: `notebooks/demo.ipynb`
2. Select the `.venv` kernel when prompted
3. The `ipykernel` dependency is already included in the dev dependencies

**Note:** To use the *.venv* inside notebooks the `ipykernel` must be installed in the *.venv*. You can install it as development dependency using:

```bash
# add specific version of ipykernel to dev
uv add --group dev "ipykernel>=6.29.5,<7"
```

## Getting Help

If you encounter issues:

1. Check the [troubleshooting guide](./troubleshooting.md).
2. Run `task help` for detailed workflow information.
