from pydantic import BaseModel
import uuid


class WorldCreateResponse(BaseModel):

    id: uuid.UUID
    path_presigned_urls: dict[str, str]