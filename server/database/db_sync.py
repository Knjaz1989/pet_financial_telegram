from sqlalchemy import create_engine, URL

from settings import config


db_url = URL.create(
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_BASE,
    host=config.DB_HOST,
    port=config.DB_PORT,
    drivername='postgresql+psycopg2'
)

engine = create_engine(db_url)
