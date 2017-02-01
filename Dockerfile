FROM python:2.7.13-alpine

RUN apk add --no-cache gcc musl-dev

EXPOSE 5000

RUN mkdir -p /application

COPY requirements.txt /application/
COPY app /application/app
COPY bot /application/bot
COPY run.py /application/

RUN pip install -r /application/requirements.txt

ENTRYPOINT python /application/run.py
