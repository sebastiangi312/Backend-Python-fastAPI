from environs import Env

env = Env()
env.read_env()

DB_ENGINE: str = env("DB_ENGINE")
DB_IP: str = env("DB_IP")
DB_PORT: str = env("DB_PORT")


class Config:
    CONNECTION_STR = f"{DB_ENGINE}://{DB_IP}:{DB_PORT}/"
    DB = "csvdb"
    DB_COLLECTION = "csv_collection"
