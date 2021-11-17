FROM python:3.8-slim-buster

WORKDIR /www

COPY . /www

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip

RUN pip3 install Flask gunicorn

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
