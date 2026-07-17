from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest

from exceptions.world_not_found_exception import WorldNotFoundException

import uuid
import aioboto3

import config


class WorldStorageRepository:


    def __init__(self) -> None:
        pass


    async def add_world(self, world_create_request: WorldCreateRequest) -> WorldResponse:
        
        session = aioboto3.Session()

        async with session.client( #type: ignore (aws runtime gen thing)
            "s3",
            endpoint_url=config.CLOUD_ENDPOINT_URL,
            aws_access_key_id=config.CLOUD_ACCESS_KEY_ID,
            aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY,
        ) as s3_client:
            
            await s3_client.put_object(Bucket="craftsync-worlds", Key=f"worlds/{world_create_request.id}", Body=b"")


        return WorldResponse(
            id = world_create_request.id
        )


    async def delete_world_by_id(self, id: uuid.UUID) -> None:

        pass
    



