class Settings:

    BOT_TOKEN: str

    class Config:
        env_file = '../develop.env'

config = Settings()
