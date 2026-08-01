from models.responses.world_create_response import WorldCreateResponse
from models.requests.world_update_request import WorldUpdateRequest
from models.requests.world_create_request import WorldCreateRequest
from models.responses.world_update_response import WorldUpdateResponse
from exceptions.world_not_found_exception import WorldNotFoundException
from models.responses.world_download_response import WorldDownloadResponse

import uuid
import aioboto3

import config


class WorldStorageRepository:


    def __init__(self) -> None:

        self.session = aioboto3.Session()


    async def add_world(self, id, world_create_request: WorldCreateRequest) -> WorldCreateResponse:

        path_urls = {}

        async with self.session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore
            
            for path in world_create_request.relative_paths:
                path_urls[path] = await s3_client.generate_presigned_url("put_object", Params={"Bucket": config.CLOUD_BUCKET_NAME, "Key": f"worlds/{id}/{path}"}, ExpiresIn=600)

        return WorldCreateResponse(
            path_presigned_urls=path_urls
        )


    async def delete_world_by_id(self, id: uuid.UUID) -> None:

        object_keys: list[dict[str, str]] = []

        async with self.session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore

            #getting object keys
            paginator = s3_client.get_paginator("list_objects_v2")
            async for page in paginator.paginate(Bucket=config.CLOUD_BUCKET_NAME, Prefix=f"worlds/{str(id)}"):

                try:
                    for object in page["Contents"]: 
                        #setting key pair for s3 translation
                        object_keys.append({"Key": object["Key"]})
                #nonreal id
                except KeyError:
                    raise WorldNotFoundException

            await s3_client.delete_objects(
                Bucket=config.CLOUD_BUCKET_NAME,
                Delete={"Objects": object_keys}
            )


    async def update_world_by_id(self, id: uuid.UUID, world_update_request: WorldUpdateRequest) -> WorldUpdateResponse:

        #this tracks all unchanged files, as told by the client request
        keys_to_delete: list[dict[str, str]] = []
        presigned_urls = {}

        async with self.session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore

            #getting object keys
            paginator = s3_client.get_paginator("list_objects_v2")
            async for page in paginator.paginate(Bucket=config.CLOUD_BUCKET_NAME, Prefix=f"worlds/{str(id)}"):
                for object in page["Contents"]: 

                    if object["Key"] in world_update_request.relative_paths:
                        #setting key pair for s3 translation
                        keys_to_delete.append({"Key": object["Key"]})
                        continue
                    
                    presigned_urls[object["Key"].removeprefix(f"worlds/{id}/")] = await s3_client.generate_presigned_url("get_object", Params={"Bucket": config.CLOUD_BUCKET_NAME, "Key": object["Key"]})

            await s3_client.delete_objects(
                Bucket=config.CLOUD_BUCKET_NAME,
                Delete={"Objects": keys_to_delete}
            )

        return WorldUpdateResponse(
            path_presigned_urls=presigned_urls
        )


    async def download_world_by_id(self, id: uuid.UUID) -> WorldDownloadResponse:

        presigned_urls = {}

        #we use region specification
        async with self.session.client("s3", endpoint_url=config.CLOUD_ENDPOINT_URL, aws_access_key_id=config.CLOUD_ACCESS_KEY_ID, aws_secret_access_key=config.CLOUD_SECRET_ACCESS_KEY) as s3_client: #type: ignore

            #the whole concept is to get the paths so you can reference them from s2 to get presigned urls.
            paginator = s3_client.get_paginator("list_objects_v2")
            async for page in paginator.paginate(Bucket=config.CLOUD_BUCKET_NAME, Prefix=f"worlds/{str(id)}"):
                for object in page.get("Contents", []):
                    presigned_urls[object["Key"].removeprefix(f"worlds/{id}/")] = await s3_client.generate_presigned_url("get_object", Params={"Bucket": config.CLOUD_BUCKET_NAME, "Key": object["Key"]})
            
        return WorldDownloadResponse(   
            path_presigned_urls = presigned_urls
        )







