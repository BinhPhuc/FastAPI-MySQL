from sqlmodel import Session, select

from models.hero import Hero, HeroCreate
from services.hero_service_interface import HeroServiceInterface

class HeroService(HeroServiceInterface):
    def get_hero(self, hero_id: int, session: Session):
        hero = session.get(Hero, hero_id)
        return hero

    def get_all_heroes(self, session: Session):
        heroes = session.exec(select(Hero)).all()
        return heroes

    def create_hero(self, hero_data: HeroCreate, session: Session):
        hero = Hero(
            name=hero_data.name,
            secret_name=hero_data.secret_name,
            age=hero_data.age
        )
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero

    def update_hero(self, hero_id: int, hero_data: HeroCreate, session: Session):
        hero = session.get(Hero, hero_id)
        if not hero:
            return None
        hero.name = hero_data.name
        hero.secret_name = hero_data.secret_name
        hero.age = hero_data.age
        session.commit()
        session.refresh(hero)
        return hero