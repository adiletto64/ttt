FROM python:3.11-slim

WORKDIR /app

RUN pip install pika

COPY . /app

CMD ["python", "main.py"]

