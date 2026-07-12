from contextlib import asynccontextmanager
import fastapi

from repositories.repository_base import RepositoryBase


#this function is stinky... but it does the job and is for sqlite dev only
def create_lifespan(repositories: list[RepositoryBase]):
    """The pre-launch repository database initialization function."""
    @asynccontextmanager
    async def lifespan(app: fastapi.FastAPI):
        for repository in repositories:
            await repository.initialize_database()
        yield
    return lifespan
