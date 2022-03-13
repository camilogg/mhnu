# pull official base image
FROM python:3.9-slim-bullseye

LABEL MAINTAINER="adrian.gonzalez@unillanos.edu.co"

# set work directory
WORKDIR /backend

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    wait-for-it && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install

# copy entrypoint.sh
COPY ./entrypoint.sh /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh

# copy project
COPY . .

RUN adduser app
USER app

# run entrypoint.sh
ENTRYPOINT ["/backend/entrypoint.sh"]