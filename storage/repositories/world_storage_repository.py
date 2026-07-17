from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest
from botocore.config import Config

from exceptions.world_not_found_exception import WorldNotFoundException

import uuid
import aioboto3

import config


class WorldStorageRepository:


    def __init__(self) -> None:
        pass


    async def add_world(self, world_create_request: WorldCreateRequest) -> WorldResponse:
        
        session = aioboto3.Session()

        async with session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore
            
            await s3_client.put_object(Bucket="craftsync", Key=f"worlds/{world_create_request.id}")
            url_to_send = await s3_client.generate_presigned_url("put_object", Params={"Bucket": "craftsync", "Key": f"worlds/{world_create_request.id}"}, ExpiresIn=600)

        return WorldResponse(
            id = world_create_request.id,
            presigned_url=url_to_send
        )


    async def delete_world_by_id(self, id: uuid.UUID) -> None:

        pass
    



