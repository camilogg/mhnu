FROM python:3.9.0-slim-buster
LABEL MAINTAINER="adrian.gonzalez@unillanos.edu.co"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update && apt-get install -y gettext
WORKDIR /src
COPY requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /src/
EXPOSE 9000

#RUN useradd user
#RUN chown -R user:user /src
#RUN chmod -R 755 /src
#USER user