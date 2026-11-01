# ERP Backend

## Local MySQL connection

The backend connects to the `erp` MySQL database on `127.0.0.1:3306`. Copy
`.env.example` to `.env` and set `DB_USER` and `DB_PASSWORD` to your local MySQL
credentials. `.env` is ignored by Git.

Install dependencies and start the API from this directory:

```powershell
uv sync --no-install-project
uv run uvicorn main:app --reload
```

Verify database connectivity at `http://127.0.0.1:8000/health/database`. A
successful response includes `{"status":"connected","database":"erp"}`.