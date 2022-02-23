# syntax=docker/dockerfile:1
FROM python:3.10.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /docker

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r requirements.txt

ENV PATH='/docker/venv/bin:$PATH'

COPY /alembic.ini /docker/
COPY /alembic /docker/alembic
COPY /app /docker/app

CMD uvicorn app.main:app --host 0.0.0.0 --no-server-header