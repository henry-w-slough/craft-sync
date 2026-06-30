import datetime


class World:

    def __init__(self, name: str, description: str) -> None:
            
        self.name: str = name
        self.description: str = description
        self.date_added: datetime.datetime = datetime.datetime.now()
