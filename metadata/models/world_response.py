from pydantic import BaseModel
import datetime


class WorldResponse(BaseModel):

    name: str
    description: str
    date_added: datetime.datetime