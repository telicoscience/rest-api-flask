APP = restapi 

test: 
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings
compose: 
	@docker compose build 
	@docker compose up
heroku: 
	@heroku container:push -a comunidadedevops-restapi web
	@heroku container:release -a comunidadedevops-restapi web 