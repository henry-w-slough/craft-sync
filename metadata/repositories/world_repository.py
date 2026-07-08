import aiosqlite
import uuid
import datetime

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
        async with aiosqlite.connect(self.db_conn_path) as db:

            await db.execute("""
                CREATE TABLE IF NOT EXISTS worlds (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    date_added TEXT
                )
            """)

            await db.commit()
            

    async def add_world(self, world: World) -> World:
        
        async with aiosqlite.connect(self.db_conn_path) as db:

            await db.execute(
                "INSERT INTO worlds (id, name, description, date_added) VALUES (?, ?, ?, ?)",
                (str(world.id), world.name, world.description, str(world.date_added),)
            )
            await db.commit()

        return world
    

    async def delete_world_by_id(self, id: uuid.UUID) -> None:

        async with aiosqlite.connect(self.db_conn_path) as db:

            await db.execute(
                "DELETE FROM worlds WHERE id = ?",
                (str(id),)
            )
            await db.commit()



