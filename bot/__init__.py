from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('key_word_id', Integer, ForeignKey('key_word.id')),
                          Column('response_id', Integer, ForeignKey('response.id'))
                          )


class KeyWord(Base):
    __tablename__ = 'key_word'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))
    response = relationship("Response",
                            secondary=association_table)

    def __str__(self):
        return self.text


class Response(Base):
    __tablename__ = 'response'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))

    def __str__(self):
        return self.text


engine = create_engine('sqlite:///')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(KeyWord(text='hello', response=[Response(text='HELLO')]))


def get_response(text):
    tokens = text.split(' ')
    response = session.query(KeyWord).filter(KeyWord.text == tokens[0]).first()
    if response.response[0]:
        return response.response[0].text
