from abc import ABC, abstractmethod
from sqlmodel import Session

from src.models.hero import HeroCreate

class HeroServiceInterface(ABC):
    @abstractmethod
    def get_hero(self, hero_id: int, session: Session):
        """Get a hero by ID"""
        pass

    @abstractmethod
    def get_all_heroes(self, session: Session):
        """Get all heroes"""
        pass

    @abstractmethod
    def create_hero(self, hero_data: HeroCreate, session: Session):
        """Create a new hero"""
        pass

    @abstractmethod
    def update_hero(self, hero_id: int, hero_data: HeroCreate, session: Session):
        """Update an existing hero"""
        pass