FROM python:3.10-slim

WORKDIR /app/habit

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
