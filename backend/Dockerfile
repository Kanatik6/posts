FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .


RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt


COPY . .