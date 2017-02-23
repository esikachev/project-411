import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

if Base:
    from models import KeyWord, Response

engine = create_engine(os.environ.get("DATABASE_URL", 'sqlite:///'))
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(KeyWord(text='hello', response=[Response(text='HELLO')]))


def get_response(text):
    tokens = text.split(' ')
    response = session.query(KeyWord).filter(KeyWord.text == tokens[0]).first()
    if response.response[0]:
        return response.response[0].text
