from abc import ABC, abstractmethod

from sqlmodel import Session

from src.models.team import TeamCreate

class TeamServiceInterface(ABC):
    @abstractmethod
    def get_team(self, team_id: int, session: Session):
        """Get a team by ID"""
        pass

    @abstractmethod
    def get_all_teams(self, session: Session):
        """Get all teams"""
        pass

    @abstractmethod
    def create_team(self, team_dto: TeamCreate, session: Session):
        """Create a new team"""
        pass

    @abstractmethod
    def update_team(self, team_id: int, team_dto: TeamCreate, session: Session):
        """Update an existing team"""
        pass