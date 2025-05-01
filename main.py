from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Path, Depends
from sqlmodel import Session

from models.hero import (Hero, HeroCreate, HeroResponse)
from db import init_db, get_session
from services.hero_service import HeroService


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the db
    init_db()
    yield
    # Cleanup code can be added here if needed

app = FastAPI(lifespan=lifespan)

hero_service = HeroService()

@app.get("/")
async def sample():
    return {"message": "Hello, World!"}

@app.get("/heroes")
async def get_heroes(
        session: Session = Depends(get_session)
):
    heroes = hero_service.get_all_heroes(session)
    return [HeroResponse.model_validate(hero) for hero in heroes]
    # Using model_validate for convert to HeroResponse

@app.get("/heroes/{hero_id}")
async def get_hero_by_id(
        hero_id: int = Path(..., title="The ID of the hero to retrieve"),
        session: Session = Depends(get_session)
):
    hero = hero_service.get_hero(hero_id, session)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return HeroResponse.model_validate(hero)

@app.post("/heroes")
async def create_hero(
        hero_dto: HeroCreate,
        session: Session = Depends(get_session)
):
    hero = hero_service.create_hero(hero_dto, session)
    return {"message": "Hero created", "hero": hero}

@app.put("/heroes/{hero_id}")
async def update_hero(
        hero_dto: HeroCreate,
        hero_id: int = Path(..., title="The ID of the hero to update"),
        session: Session = Depends(get_session)
):
    hero = hero_service.update_hero(hero_id, hero_dto, session)
    return {"message": "Hero updated", "hero": hero}