from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from bot import Base

association_table = Table('association', Base.metadata,
                          Column('key_word_id',
                                 Integer,
                                 ForeignKey('key_word.id')),
                          Column('response_id',
                                 Integer,
                                 ForeignKey('response.id'))
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