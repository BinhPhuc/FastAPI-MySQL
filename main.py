from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import Hero, HeroCreate, HeroResponse
from database import init_db, get_session
from sqlmodel import Session, select

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

@app.get("/heroes")
async def get_heroes(
        session: Session = Depends(get_session)
):
    heroes = session.exec(select(Hero))
    return [HeroResponse.model_validate(hero) for hero in heroes]
    # Using model_validate for convert to HeroResponse

@app.get("/heroes/{hero_id}")
async def get_hero_by_id(
        hero_id: int = Path(..., title="The ID of the hero to retrieve"),
        session: Session = Depends(get_session)
):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return HeroResponse.model_validate(hero)

@app.post("/heroes")
async def create_hero(
        hero_dto: HeroCreate,
        session: Session = Depends(get_session)
):
    # Here you would typically add the hero to the database
    hero = Hero(
        name=hero_dto.name,
        secret_name=hero_dto.secret_name,
        age=hero_dto.age
    )
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return {"message": "Hero created", "hero": hero_dto}
