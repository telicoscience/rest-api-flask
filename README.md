# rest-api-flask (Flask + MongoDB)

REST API built with Flask and Flask-RESTful, using MongoDB via MongoEngine.
The project focuses on clean configuration per environment, containerized setup, and automated testing/pipeline.

## Tech Stack
- Python + Flask + Flask-RESTful
- MongoDB (MongoEngine)
- Docker / Docker Compose
- Pytest (fixtures)
- GitHub Actions (CI)
- Insomnia (local + production collections)

## Features (Current)
- Create user (POST)
- List users (GET)
- Get user by CPF (GET)
- Update user (PATCH) — implemented
- CPF validation (check digits)
- Proper error handling for user not found
- Environment configs (dev/prod/mock)
- Application Factory pattern (decoupled app)
- Dockerized API + MongoDB (Compose)
- CI pipeline with secrets

## API Endpoints (Example)
Base URL: `http://localhost:5000`

- `GET /health` (planned)
- `POST /users`
- `GET /users`
- `GET /users/<cpf>`
- `PATCH /users/<cpf>`
- `DELETE /users/<cpf>` (planned)

## Running locally (venv)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python wsgi.py
