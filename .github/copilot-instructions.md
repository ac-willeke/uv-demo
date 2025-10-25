# Copilot Instructions

This file provides guidelines for GitHub Copilot to assist in code and documentation generation for Python projects.

This file must be located in `.github/copilot-instructions.md`

## Project Overview

- Purpose: A demo repository showcasing Python project development and packaging best practices using UV.
- Tech stack: Python, Docker, GitHub Actions
- Target audience: Junior to mid-level developers learning Python package development and CI/CD

## Documentation Standards
- English, clear and concise, active voice
- Maintain a neutral and professional tone
- No exaggeration, promotional language, or superlatives
- No emoticons or emojis
- Avoid adverbs and adjectives
- Avoid duplication and redundancy, link to existing docs instead or refer to official sources.
- `/docs`: Python development guides and best practices

## Python Standards

### Code Style
- PEP8
- Use double quotes for strings
- Use f-strings for string formatting
- Use `%` for string formatting in log messages
- Add type hints to all functions and methods
- Import order: standard library, third-party, local modules

### Code Documentation
- inline comments: Do not add explanatory comments to code unless requested
- docstrings: reStructuredText (reST) style
- docstrings for all functions, classes, and modules

### Performance
- Use generators over lists for large datasets
- Context managers for resource management
- Avoid global variables
- Use lazy evaluation where possible

### Function Design
- Use functional programming principles
- Single responsibility functions
- Functional programming principles (avoid classes unless requested)

### Function Example
```python
def rename_columns(
    df: DataFrame,
    mapping: Dict[str, str],
    **kwargs: Any
) -> DataFrame:
    """
    Rename columns using mapping dictionary.

    :param df: Input Spark DataFrame.
    :param mapping: Dictionary mapping old to new column names.
    :return: DataFrame with renamed columns.
    """
    for old_name, new_name in mapping.items():
        if old_name in df.columns and old_name != new_name:
            logger.info("RENAMING COLUMN: %s -> %s", old_name, new_name)
            df = df.withColumnRenamed(old_name, new_name)
    return df
```
