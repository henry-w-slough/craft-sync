from pydantic import BaseModel
import uuid


class WorldResponse(BaseModel):

    id: uuid.UUID