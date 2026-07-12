from pydantic import BaseModel, Field


class WorldCreateRequest(BaseModel):

    name: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=1000)