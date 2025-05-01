from sqlmodel import Field, SQLModel, Relationship
from typing import Annotated

from .team import Team

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(..., title="Hero name", max_length=100, index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")

class HeroCreate(SQLModel): # Same as HeroDTO in Java Spring Boot
    name: Annotated[str, Field(..., title="Hero name", max_length=100)]
    secret_name: Annotated[str, Field(..., title="Secret name", max_length=100)]
    age: Annotated[int | None, Field(default=None, title="Hero age")]
    team_id: Annotated[int | None, Field(default=None, title="Team ID")]

class HeroResponse(SQLModel):
    name: str
    secret_name: str
    age: int | None = None
    team_id: int | None = None