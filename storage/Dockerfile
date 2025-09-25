FROM python:3.12

RUN apt-get update

WORKDIR /src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN if [ -f .env.production ]; then cp .env.production .env; fi