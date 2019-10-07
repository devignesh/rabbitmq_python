#!/usr/bin/env_python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1:8000'))
channel = connection.channel()
channel.queue_declare(queue='vickymsgque')

channel.basic_publish(exchange='', routing_key='msg', body='hi vicky')
# print(" [x] Sent 'hi vicky'")
connection.close()