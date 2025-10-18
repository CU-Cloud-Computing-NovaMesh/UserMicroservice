# UserMicroservice
Repo for user microservice

A minimal FastAPI microservice for managing users in a second-hand marketplace.

## What’s included (Sprint 1)
- REST paths for `POST /users`, `GET /users/{id}`, `PUT /users/{id}`, `DELETE /users/{id}` (currently return **501 NOT IMPLEMENTED**).
- Pydantic models for request/response → auto-generated **OpenAPI** docs.
- MySQL relational schema (`schema.sql`).

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001

```

- Swagger UI: http://localhost:8001/docs  
- OpenAPI JSON: http://localhost:8001/openapi.json


## Database schema
See `schema.sql`.
