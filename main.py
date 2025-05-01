from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.db import init_db
from src.controllers import all_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the db
    init_db()
    yield
    # Cleanup code can be added here if needed

app = FastAPI(lifespan=lifespan)

for router in all_routers:
    app.include_router(router)