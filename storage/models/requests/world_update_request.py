from pydantic import BaseModel


class WorldUpdateRequest(BaseModel):
    
    file_paths: list[str]