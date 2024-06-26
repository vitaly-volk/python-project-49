install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --break-system-packages

make-lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games
