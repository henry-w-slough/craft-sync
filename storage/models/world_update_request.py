from pydantic import BaseModel
import uuid


class WorldUpdateRequest(BaseModel):

    id: uuid.UUID