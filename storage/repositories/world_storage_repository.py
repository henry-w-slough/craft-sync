from models.world_response import WorldResponse
from models.world_create_response import WorldCreateResponse
from models.world_response import WorldResponse
from models.world_update_request import WorldUpdateRequest
from models.world_create_request import WorldCreateRequest

from botocore.exceptions import ClientError

from exceptions.world_not_found_exception import WorldNotFoundException

import uuid
import aioboto3
import asyncio

import config


class WorldStorageRepository:


    def __init__(self) -> None:
        pass


    async def add_world(self, id, world_create_request: WorldCreateRequest) -> WorldCreateResponse:
        
        session = aioboto3.Session()

        path_urls = {}

        async with session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore
            
            for path in world_create_request.relative_paths:
                path_urls[path] = await s3_client.generate_presigned_url("put_object", Params={"Bucket": config.CLOUD_BUCKET_NAME, "Key": f"worlds/{id}/{path}"}, ExpiresIn=600)

        return WorldCreateResponse(
            id = id,
            path_presigned_urls=path_urls
        )


    async def delete_world_by_id(self, id: uuid.UUID) -> None:

        session = aioboto3.Session()

        async with session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore

            try:
                #object verification
                await s3_client.head_object(Bucket=config.CLOUD_BUCKET_NAME, Key=f"worlds/{id}")
                await s3_client.delete_object(Bucket=config.CLOUD_BUCKET_NAME, Key=f"worlds/{id}")
            except ClientError:
                raise WorldNotFoundException
            

    async def update_world_by_id(self, id: uuid.UUID, world_update_request: WorldUpdateRequest) -> WorldResponse:

        session = aioboto3.Session()

        async with session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore
            
            try:
                await s3_client.head_object(Bucket=config.CLOUD_BUCKET_NAME, Key=f"worlds/{id}")
                await s3_client.put_object(Bucket=config.CLOUD_BUCKET_NAME, Key=f"worlds/{id}")
                url_to_send = await s3_client.generate_presigned_url("put_object", Params={"Bucket": config.CLOUD_BUCKET_NAME, "Key": f"worlds/{id}"}, ExpiresIn=600)
            except ClientError:
                raise WorldNotFoundException

        return WorldResponse(
            id = id,
            presigned_url = url_to_send
        )





