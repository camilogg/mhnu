FROM python:slim-bullseye

LABEL MAINTAINER="adrian.gonzalez@unillanos.edu.co"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    wait-for-it && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
