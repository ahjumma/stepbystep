lint:
	python -m flake8 stepbystep tests
	python -m isort --profile black --check-only stepbystep tests
	python -m black --check stepbystep tests

format:
	python -m isort --profile black stepbystep tests
	python -m black stepbystep tests

test: lint
	EDITOR=vim python -m pytest --cov=stepbystep --cov-fail-under=58
	python -m mypy -p stepbystep
	python -m mypy -p tests

setup:
	python -m pip install -Ur requirements.txt

