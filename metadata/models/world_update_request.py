from pydantic import BaseModel
import uuid


class WorldUpdateRequest(BaseModel):

    name: str | None = None
    description: str | None = None