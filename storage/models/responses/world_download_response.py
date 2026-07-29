from pydantic import BaseModel


class WorldDownloadResponse(BaseModel):

    path_presigned_urls: dict[str, str]