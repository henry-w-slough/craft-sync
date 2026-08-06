from pydantic import BaseModel


class WorldCreateRequest(BaseModel):
    
    file_paths: list[str]