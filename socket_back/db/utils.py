import os

from socket_back.settings import settings


def create_database() -> None:
    """Create a database."""


def drop_database() -> None:
    """Drop current database."""
    if settings.db_file.exists():
        os.remove(settings.db_file)
