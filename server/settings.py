from pydantic import BaseSettings


class Settings(BaseSettings):

    BOT_TOKEN: str

    #db
    DB_USER: str = ''
    DB_PASSWORD: str = ''
    DB_BASE: str = ''
    DB_HOST: str = ''
    DB_PORT: int = 0000

    class Config:
        env_file = '../develop.env'


config = Settings()
