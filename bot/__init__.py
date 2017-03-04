from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if Base:
    from models import Request, Response

engine = create_engine('sqlite:///bot.db')
Base.metadata.create_all(engine)
