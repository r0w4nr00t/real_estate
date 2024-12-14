run:
	poetry run python3 -m real_estate.manage runserver
shell:
	poetry run python3 -m real_estate.manage shell

migrations:
	poetry run python3 -m real_estate.manage makemigrations
	poetry run python3 -m real_estate.manage migrate

su:
	poetry run python3 -m real_estate.manage createsuperuser

showmigrations:
	poetry run python3 -m real_estate.manage showmigrations

flush:
	poetry run python3 -m real_estate.manage flush
