FROM ubuntu:latest

WORKDIR /appli

COPY . /appli

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip

RUN pip3 install Flask gunicorn

RUN apt update && apt install -y \
    libmariadb3 \
    libmariadb-dev

#CMD [ "python3", "app.py"]
CMD [ "flask", "run"]
