from models.responses.world_create_response import WorldCreateResponse
from models.requests.world_update_request import WorldUpdateRequest
from models.requests.world_create_request import WorldCreateRequest
from models.responses.world_update_response import WorldUpdateResponse
from exceptions.world_not_found_exception import WorldNotFoundException
from models.responses.world_download_response import WorldDownloadResponse

import uuid
import aioboto3
from botocore.config import Config

import config


class WorldStorageRepository:


    def __init__(self) -> None:

        self.session = aioboto3.Session()

        self.session_config = Config(signature_version="s3v4", s3={"addressing_style": "path"})


    async def add_world(self, id: uuid.UUID, world_create_request: WorldCreateRequest) -> WorldCreateResponse:

        presigned_urls = {}

        async with self.session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY, config=self.session_config) as s3_client: #type: ignore
            
            for path in world_create_request.file_paths:
                presigned_urls[path] = await s3_client.generate_presigned_url("put_object", Params={"Bucket": config.CLOUD_BUCKET_NAME, "Key": f"worlds/{id}/{path}"}, ExpiresIn=600)

        return WorldCreateResponse(
            path_presigned_urls=presigned_urls
        )


    async def update_world(self, id: uuid.UUID, world_update_request: WorldUpdateRequest) -> None:

        presigned_urls = {}

        async with self.session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY, config=self.session_config) as s3_client: #type: ignore

            for path in world_update_request.file_paths:
                presigned_urls[path] = await s3_client.generate_presigned_url("put_object", Params={"Bucket": config.CLOUD_BUCKET_NAME, "Key": f"worlds/{id}/{path}"}, ExpiresIn=600)


    async def download_world(self) -> None:
        pass


    async def delete_world(self) -> None:
        pass
  
