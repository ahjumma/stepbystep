lint:
	python -m flake8 stepbystep
	python -m isort --profile black --check-only stepbystep
	python -m black --check stepbystep

format:
	python -m isort --profile black stepbystep
	python -m black stepbystep

test: lint
	python -m pytest --cov=stepbystep --cov-fail-under=58
	python -m mypy stepbystep/*.py

setup:
	python -m pip install -Ur requirements.txt

