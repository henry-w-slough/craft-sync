from abc import ABC, abstractmethod


class RepositoryBase(ABC):
    """
    Prepares database for storage by adding necessary tables to it.
    """

    @abstractmethod
    async def initialize_database(self) -> None:
        pass
    