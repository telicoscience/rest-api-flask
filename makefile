VERCEL_PROJECT = rest-api-flask 

test: 
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings
compose: 
	@docker compose build 
	@docker compose up
heroku: 
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web
vercel:
	@echo "Iniciando deploy na Vercel..."
	vercel --prod