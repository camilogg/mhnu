# pull official base image
FROM python:3.9-slim-bullseye

LABEL MAINTAINER="adrian.gonzalez@unillanos.edu.co"

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PATH /home/app/.local/bin:$PATH

# install dependencies
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    wait-for-it && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# set user
RUN useradd -m app
USER app

# set work directory
WORKDIR /backend

RUN pip install --user --upgrade pip poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/backend/entrypoint.sh"]