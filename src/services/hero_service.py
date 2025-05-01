from sqlmodel import Session, select

from src.models.hero import Hero, HeroCreate
from src.services.hero_service_interface import HeroServiceInterface

class HeroService(HeroServiceInterface):
    def get_hero(self, hero_id: int, session: Session):
        hero = session.get(Hero, hero_id)
        if not hero:
            return None
        return hero

    def get_all_heroes(self, session: Session):
        heroes = session.exec(select(Hero)).all()
        return heroes

    def create_hero(self, hero_dto: HeroCreate, session: Session):
        hero = Hero(
            name=hero_dto.name,
            secret_name=hero_dto.secret_name,
            age=hero_dto.age,
            team_id=hero_dto.team_id
        )
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero

    def update_hero(self, hero_id: int, hero_dto: HeroCreate, session: Session):
        hero = session.get(Hero, hero_id)
        if not hero:
            return None
        hero.name = hero_dto.name
        hero.secret_name = hero_dto.secret_name
        hero.age = hero_dto.age
        hero.team_id = hero_dto.team_id
        session.commit()
        session.refresh(hero)
        return hero