from pydantic import BaseSettings,Field
from pathlib import WindowsPath
from functools import lru_cache
import pathlib,os

os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT']="1"

BASE_DIR = ASTRADB_CONNECT_BUNDLE = pathlib.Path(__file__).parent

class Settings(BaseSettings):
    keyspace: str = Field(...,env="ASTRADB_KEYSPACE")
    base_dir: WindowsPath = BASE_DIR
    db_client_id:str = Field(...,env="ASTRADB_CLIENT_ID")
    db_client_secret:str = Field(...,env="ASTRADB_CLIENT_SECRET")

    class Config:
        env_file = BASE_DIR.parent / '.env'

@lru_cache
def get_settings():
    return Settings()