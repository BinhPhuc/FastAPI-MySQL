from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Path, Query
from models import Hero
from database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database
    init_db()
    yield
    # Cleanup code can be added here if needed
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def sample():
    return {"message": "Hello, World!"}
