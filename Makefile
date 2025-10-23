make env-add:
	pdm add ${pkgs}

env-add-dev:
	pdm add -dG test ${pkgs}

lint:
	pdm run lint

test:
	pdm run pytest tests/