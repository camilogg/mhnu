FROM python:3.9.0-slim-buster
LABEL MAINTAINER="adrian.gonzalez@unillanos.edu.co"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update && apt-get install -y gettext libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    libffi-dev shared-mime-info wait-for-it && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /src
COPY requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /src/
EXPOSE 8000
