import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config

db_engine = create_engine(...)
SessionFactory = sessionmaker(bind=db_engine)
db_session: sqlalchemy.orm.Session = SessionFactory()
