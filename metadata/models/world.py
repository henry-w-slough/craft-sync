import datetime
import uuid

class World:

    def __init__(self, name: str, description: str, id: uuid.UUID | None = None, date_added: datetime.datetime | None = None) -> None:
            
        self.name: str = name
        self.description: str = description
        #optional params for World when recreating a full World
        self.date_added: datetime.datetime = date_added if date_added is not None else datetime.datetime.now()
        self.id: uuid.UUID = id if id is not None else uuid.uuid4()
