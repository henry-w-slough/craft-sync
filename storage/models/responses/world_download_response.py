from pydantic import BaseModel


class WorldDownloadResponse(BaseModel):

    presigned_urls: list[str]