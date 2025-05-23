import pika
import os
import time

rabbitmq_url = os.getenv("RABBITMQ_URL")

params = pika.URLParameters(rabbitmq_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='test_queue')
channel.basic_publish(exchange='', routing_key='test_queue', body='Hello from Python!')
print("Message sent to RabbitMQ")
connection.close()
