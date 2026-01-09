# Build log — rest-api-flask

A short timeline of what was implemented, in order, to make it easier to recall details during reviews and interviews.

## Build timeline
1) Repo created + SSH keys configured
2) venv + pip setup + first Flask run
3) Flask-RESTful added + reqparse for first POST
4) Linting added (flake8)
5) MongoEngine integration + basic CRUD
6) CPF validation (check digits)
7) Users listing + user-not-found handling
8) Application Factory pattern + decoupled structure
9) Dockerfile + Docker Compose adjustments
10) Insomnia collections (local + production)
11) Pytest added + fixtures + POST test
12) MongoDB Atlas setup
13) Deploy to Vercel + production environment config
14) GitHub Actions pipeline + CI secrets configured
15) PATCH route implemented

## Next steps
- Write tests for PATCH route
- Implement DELETE route
- Add /health endpoint + DB check
