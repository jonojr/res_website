FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD /requirements/base.txt /code/
ADD /requirements/development.txt /code/
RUN pip install -r development.txt

ADD . /code/
