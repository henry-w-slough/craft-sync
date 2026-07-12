import aiosqlite
import uuid
import datetime

from models.world import World
from models.world_update_request import WorldUpdateRequest

from repositories.repository_base import RepositoryBase

from exceptions.world_not_found_exception import WorldNotFoundException


class WorldMetadataRepository(RepositoryBase):


    def __init__(self) -> None:
        
        #using sqlite as temporary development database setup
        self.db_conn_path = "metadata.db"


    async def initialize_database(self) -> None:

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


    async def get_all_worlds(self) -> list[World]:

        async with aiosqlite.connect(self.db_conn_path) as db:
            
            db.row_factory = aiosqlite.Row

            sql_result = await db.execute("SELECT * FROM worlds")
            stored_worlds = sql_result.fetchall()

            #constructing all worlds based on sql rows
            all_worlds = []
            for world in await stored_worlds:
                all_worlds.append(
                    World(
                        world["name"],
                        world["description"],
                        uuid.UUID(world["id"]),
                        datetime.datetime.fromisoformat(world["date_added"])
                    )
                )
                
            return all_worlds
    

    async def add_world(self, world: World) -> World:
        
        async with aiosqlite.connect(self.db_conn_path) as db:

            await db.execute(
                "INSERT INTO worlds (id, name, description, date_added) VALUES (?, ?, ?, ?)",
                (str(world.id), world.name, world.description, str(world.date_added),)
            )
            await db.commit()

        return world
    

    async def update_world(self, world_update_request: WorldUpdateRequest, id: uuid.UUID) -> World:
        
        async with aiosqlite.connect(self.db_conn_path) as db:
            
            
            if world_update_request.name is not None or world_update_request.description is not None:

                #holds the data to be updated within the db
                fields = {}

                #checking which fields are set to be updated
                if world_update_request.name is not None:
                    fields["name"] = world_update_request.name
                if world_update_request.description is not None:
                    fields["description"] = world_update_request.description

                #creating the SQL call for what will be updated
                set_clause = ", ".join(f"{column} = ?" for column in fields)
                #the values passed into the SQl execution
                values = list(fields.values()) + [str(id)]

                await db.execute(
                    f"UPDATE worlds SET {set_clause} WHERE id = ?",
                    values
                )
                await db.commit()


            db.row_factory = aiosqlite.Row

            #getting row just updated to return
            sql_result = await db.execute("SELECT * FROM worlds WHERE id = ?", (str(id),))
            row = await sql_result.fetchone()

            if row is None:
                raise WorldNotFoundException

            return World(
                row["name"],
                row["description"],
                uuid.UUID(row["id"]),
                datetime.datetime.fromisoformat(row["date_added"]),
            )


    async def delete_world_by_id(self, id: uuid.UUID) -> None:

        async with aiosqlite.connect(self.db_conn_path) as db:
            

            sql_result = await db.execute(
                "DELETE FROM worlds WHERE id = ?",
                (str(id),)
            )

            #if the id given does not exist within the database
            if sql_result.rowcount == 0:
                raise WorldNotFoundException
            
            await db.commit()



