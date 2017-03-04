import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bot import Base
from bot import Request
from bot import Response


def get_response(request_text, human_response_text):
    if human_response_text == '#':
        response = session.query(Response).filter(Request.text == request_text).all()
        count = len(response)
        if count > 0:
            i = random.randint(0, count - 1)
            return response[i]
        else:
            return "I don't know the answer to this question, help me to answer it :)"
    else:
        # create new request
        new_request = Request()
        new_request.text = request_text

        # create new response
        new_response = Response()
        new_response.text = human_response_text

        # create new connection
        new_request.response = [new_response]

        # commit
        session.add(new_request)
        session.add(new_response)
        session.commit()

        return "Thank you! I got smarter :)"


if __name__ == '__main__':
    engine = create_engine('sqlite:///bot.db')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print get_response("Hi, what your name?", "#")
