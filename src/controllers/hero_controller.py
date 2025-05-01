from fastapi import APIRouter, HTTPException, Path, Depends
from sqlmodel import Session

from src.models import (HeroCreate, HeroResponse)
from src.db import get_session
from src.services import HeroServiceInterface
from src.services.hero_service import HeroService

router = APIRouter(prefix="/heroes", tags=["heroes"])

def get_hero_service() -> HeroServiceInterface:
    return HeroService()

@router.get("/")
async def get_heroes(
        session: Session = Depends(get_session),
        hero_service: HeroServiceInterface = Depends(get_hero_service)
):
    heroes = hero_service.get_all_heroes(session)
    return [HeroResponse.model_validate(hero) for hero in heroes]

@router.get("/{hero_id}")
async def get_hero_by_id(
        hero_id: int = Path(..., title="The ID of the hero to retrieve"),
        session: Session = Depends(get_session),
        hero_service: HeroServiceInterface = Depends(get_hero_service)
):
    hero = hero_service.get_hero(hero_id, session)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return HeroResponse.model_validate(hero)

@router.post("/")
async def create_hero(
        hero_dto: HeroCreate,
        session: Session = Depends(get_session),
        hero_service: HeroServiceInterface = Depends(get_hero_service)
):
    hero = hero_service.create_hero(hero_dto, session)
    return {"message": "Hero created", "hero": hero}

@router.put("/{hero_id}")
async def update_hero(
        hero_dto: HeroCreate,
        hero_id: int = Path(..., title="The ID of the hero to update"),
        session: Session = Depends(get_session),
        hero_service: HeroServiceInterface = Depends(get_hero_service)
):
    hero = hero_service.update_hero(hero_id, hero_dto, session)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return {"message": "Hero updated", "hero": hero}