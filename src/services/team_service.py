from sqlmodel import select, Session

from src.models.team import Team, TeamCreate
from src.services.team_service_interface import TeamServiceInterface


class TeamService(TeamServiceInterface):
    def get_team(self, team_id: int, session: Session):
        team = session.get(Team, team_id)
        if not team:
            return None
        return team

    def get_all_teams(self, session):
        teams = session.exec(select(Team)).all()
        return teams

    def create_team(self, team_dto: TeamCreate, session):
        team = Team(
            name=team_dto.name,
            headquarters=team_dto.headquarters
        )
        session.add(team)
        session.commit()
        session.refresh(team)
        return team

    def update_team(self, team_id: int, team_dto: TeamCreate, session):
        team = session.get(Team, team_id)
        if not team:
            return None
        team.name = team_dto.name
        team.headquarters = team_dto.headquarters
        session.commit()
        session.refresh(team)
        return team