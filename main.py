from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from database import engine

app = FastAPI(
    title="ERP System",
    description="Backend API for ERP System",
    version="1.0.0"
)

# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
    }


@app.get("/health/database")
def check_database():
    with engine.connect() as connection:
        database_name = connection.scalar(text("SELECT DATABASE()"))
    return {"status": "connected", "database": database_name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
