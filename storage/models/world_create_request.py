from pydantic import BaseModel
import uuid


class WorldCreateRequest(BaseModel):

    id: uuid.UUID