from fastapi import APIRouter, HTTPException, Path, Depends
from sqlmodel import Session

from src.db import get_session
from src.models import TeamResponse, TeamCreate
from src.services import TeamServiceInterface
from src.services.team_service import TeamService

router = APIRouter(prefix="/teams", tags=["teams"])

def get_team_service() -> TeamServiceInterface:
    return TeamService()

@router.get("/")
async def get_teams(
        session: Session = Depends(get_session),
        team_service: TeamServiceInterface = Depends(get_team_service)
):
    teams = team_service.get_all_teams(session)
    return [TeamResponse.model_validate(team) for team in teams]

@router.get("/{team_id}")
async def get_team_by_id(
        team_id: int = Path(..., title="The ID of the team to retrieve"),
        session: Session = Depends(get_session),
        team_service: TeamServiceInterface = Depends(get_team_service)
):
    team = team_service.get_team(team_id, session)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return TeamResponse.model_validate(team)

@router.post("/")
async def create_team(
        team_dto: TeamCreate,
        session: Session = Depends(get_session),
        team_service: TeamServiceInterface = Depends(get_team_service)
):
    team = team_service.create_team(team_dto, session)
    return {"message": "Team created", "team": TeamResponse.model_validate(team)}

@router.put("/{team_id}")
async def update_team(
        team_dto: TeamCreate,
        team_id: int = Path(..., title="The ID of the team to update"),
        session: Session = Depends(get_session),
        team_service: TeamServiceInterface = Depends(get_team_service)
):
    team = team_service.update_team(team_id, team_dto, session)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team updated", "team": TeamResponse.model_validate(team)}