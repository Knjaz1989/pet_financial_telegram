import sqlalchemy as sa
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Purchase(Base):
    __tablename__ = 'purchases'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text, nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    user_id = sa.Column(sa.Integer, nullable=False)
    date = sa.Column(sa.Date, server_default=sa.func.now())
