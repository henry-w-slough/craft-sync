import aiosqlite

from models.world import World
from repositories.repository_base import RepositoryBase


class WorldRepository(RepositoryBase):


    def __init__(self) -> None:
        
        #using sqlite as temporary development database setup
        self.db_conn_path = "metadata.db"


    async def initialize_database(self) -> None:
        """
        Prepares database for storage by adding necessary tables to it.
        """
        pass
            

    async def add_world(self, world: World) -> World:
        
        async with aiosqlite.connect(self.db_conn_path) as db:
            #db config
            db.row_factory = aiosqlite.Row
            cursor = db.cursor()

            await db.execute(
                "INSERT INTO worlds (id, name, description, date_added) VALUES (?, ?, ?, ?)",
                (world.id, world.name, world.description, world.date_added)
            )
            await db.commit()

        return world


