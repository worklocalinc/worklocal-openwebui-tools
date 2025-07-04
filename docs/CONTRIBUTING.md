# Contributing to WorkLocal OpenWebUI Tools

We love your input! We want to make contributing to this project as easy and transparent as possible.

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Pull Request Process

1. Update the README.md with details of changes to the interface.
2. Update the docs/ with any new usage examples.
3. The PR will be merged once you have the sign-off of at least one maintainer.

## Any contributions you make will be under the MIT Software License

When you submit code changes, your submissions are understood to be under the same [MIT License](LICENSE) that covers the project.

## Report bugs using GitHub's [issues](https://github.com/worklocalinc/worklocal-openwebui-tools/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/worklocalinc/worklocal-openwebui-tools/issues/new).

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening)

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/worklocalinc/worklocal-openwebui-tools.git
   cd worklocal-openwebui-tools
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Run tests:
   ```bash
   pytest
   ```

5. Run linting:
   ```bash
   flake8 src/ tests/
   black src/ tests/
   mypy src/
   ```

## Code Style

- We use [Black](https://github.com/psf/black) for code formatting
- We use [Flake8](https://flake8.pycqa.org/) for linting
- We use [MyPy](http://mypy-lang.org/) for type checking
- Maximum line length is 100 characters
- Use type hints where possible

## Testing

- Write tests for any new functionality
- Ensure all tests pass before submitting PR
- Aim for high test coverage (>80%)
- Use pytest for testing

## License

By contributing, you agree that your contributions will be licensed under its MIT License.