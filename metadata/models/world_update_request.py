from pydantic import BaseModel, Field


class WorldUpdateRequest(BaseModel):

    name: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = Field(default=None, min_length=1, max_length=1000)