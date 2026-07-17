


class WorldNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        """Exception thrown when a non-existent world is attempted to be accessed."""
        super().__init__(*args)
