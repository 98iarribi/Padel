make env-add:
	pdm add ${pkgs}

env-add-dev:
	pdm add -dG test ${pkgs}

env-sync:
	pdm sync

lint:
	pdm run lint

test:
	pdm run pytest tests/