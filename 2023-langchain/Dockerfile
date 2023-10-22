FROM python:3.11-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y htop ncdu git && apt-get clean

WORKDIR /app
ADD ./app .

RUN pip install -r requirements.txt
