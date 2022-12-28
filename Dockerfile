FROM python:3.9-slim

RUN apt -y update && apt -y upgrade
RUN apt -y install bash vim \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools twine wheel

WORKDIR /opt

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install -d
