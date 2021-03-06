from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from app.config import get_settings
import uuid

settings = get_settings()

class User(Model):
    __keyspace__ = settings.keyspace

    email = columns.Text(primary_key=True)
    id = columns.UUID(primary_key=True,default=uuid.uuid1)
    password = columns.Text()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"User(email={self.email},id={self.id})"