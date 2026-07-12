from pydantic import BaseModel
import datetime
import uuid


class WorldResponse(BaseModel):

    #NOTE: using FastAPI, we can abstract the process
    #of returning a response and leave it to the library
    #so instead we just pass a pydantic class instance with the info
    #to pass back

    name: str
    description: str
    date_added: datetime.datetime
    id: uuid.UUID