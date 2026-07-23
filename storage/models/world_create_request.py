from pydantic import BaseModel


class WorldCreateRequest(BaseModel):
    
    relative_paths: list[str]