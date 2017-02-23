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


class Response(Base):
    __tablename__ = 'response'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))


engine = create_engine('sqlite:///')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(KeyWord(text='testerino'))


def response(text):
    tokens = text.split(' ')
    print tokens
    response = session.query(KeyWord).filter(KeyWord.text == tokens[0]).first()
    print response.response.text
    if response:
        return response.text
