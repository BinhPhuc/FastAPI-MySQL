from typing import List

from sqlmodel import Field, SQLModel, Relationship


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(..., title="Team name", max_length=100, index=True)
    headquarters: str = Field(
        ..., title="Headquarters location", max_length=100
    )

class TeamCreate(SQLModel):
    name: str = Field(..., title="Team name", max_length=100)
    headquarters: str = Field(
        ..., title="Headquarters location", max_length=100
    )

class TeamResponse(SQLModel):
    name: str
    headquarters: str
