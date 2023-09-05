from databases import Database

from socket_back.settings import settings

database = Database(str(settings.db_url))
