from pydantic import BaseModel

class WorldUpdateResponse(BaseModel):

    path_presigned_urls: dict[str, str]