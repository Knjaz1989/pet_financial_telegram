from pydantic import BaseSettings


class Settings(BaseSettings):

    BOT_TOKEN: str

    class Config:
        env_file = '../develop.env'


config = Settings()
