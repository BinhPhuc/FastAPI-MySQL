from sqlmodel import Field, SQLModel
from typing import Annotated

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

class HeroCreate(SQLModel): # Same as HeroDTO in Java Spring Boot
    name: Annotated[str, Field(..., title="Hero name", max_length=100)]
    secret_name: Annotated[str, Field(..., title="Secret name", max_length=100)]
    age: Annotated[int | None, Field(default=None, title="Hero age")]

class HeroResponse(SQLModel):
    name: str
    secret_name: str
    age: int | None = None