from pydantic import BaseModel


class WorldCreateResponse(BaseModel):

    path_presigned_urls: dict[str, str]