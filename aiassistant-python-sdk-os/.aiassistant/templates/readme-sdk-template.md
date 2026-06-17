# Package Name

[![CI](https://github.com/OWNER/REPOSITORY/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPOSITORY/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/PACKAGE_NAME.svg)](https://pypi.org/project/PACKAGE_NAME/)

Short SDK description.

## Installation

```bash
pip install PACKAGE_NAME
```

## Quick Start

```python
from IMPORT_NAME import Client

client = Client(api_key="YOUR_API_KEY")
result = client.example_method()
print(result)
```

## Public API

Describe public imports, facade/client, domain namespaces, models, config
objects, and exceptions.

## Configuration

Document authentication, endpoints, timeouts, TLS, retries, and environment
variables.

## Examples

Link to `examples/` or `use_cases/`.

## Documentation

Link to published docs.

## Development

```bash
python -m pip install -e .[dev,docs]
python -m black --check src tests examples
python -m mypy src
python -m pytest tests/unit tests/functional -v
python -m build
twine check dist/*
```

## License

Add license.

