from abc import ABC, abstractmethod


class RepositoryBase(ABC):

    @abstractmethod
    async def initialize_database(self) -> None:
        pass
    