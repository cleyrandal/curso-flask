install:
	python -m pip install --upgrade pip
	pip install -e .['dev']


clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

init_db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db upgrade

test:
	FLASK_DEBUG=False pytest tests/ -v --cov=delivery

format:
	isort **/*.py
	black -l 79 **/*.py

run:
	FLASK_APP=delivery/app.py FLASK_ENV=production flask run

run_development:
	FLASK_APP=delivery/app.py FLASK_ENV=development flask run
