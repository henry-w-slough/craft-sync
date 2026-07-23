from pydantic import BaseModel


class WorldUpdateRequest(BaseModel):
    
    relative_paths: list[str]