# Myriad Chess

Multiple chess AIs implemented as API endpoints in Python.

## Getting Started

### Requirements

- [pipenv](https://pipenv.pypa.io/en/latest)

### Installation

```bash
git clone git@github.com:AnimeAllstar/myriad-chess.git
cd myriad-chess
pipenv install
pipenv shell
pre-commit install # installs pre-commit git hooks
uvicorn main:app --reload # runs the server on localhost:8000
```

### Other Commands

```bash
pre-commit run --all-files # runs all pre-commit hooks manually
```

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com)
- [python-chess](https://python-chess.readthedocs.io/en/latest)
