from ormar import ModelMeta

from socket_back.db.config import database
from socket_back.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
