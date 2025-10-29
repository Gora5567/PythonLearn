lint:
	flake8 . --count --show-source --statistics --exclude  .venv,build,dist
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude  .venv,build,dist

test:
	pytest .

check: lint test
