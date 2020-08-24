FROM python:3.6-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=false
ENV PYTHONPATH /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app
