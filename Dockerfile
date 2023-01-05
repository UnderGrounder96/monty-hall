FROM python:alpine

WORKDIR /code

COPY . .

CMD python3 monty-hall.py
