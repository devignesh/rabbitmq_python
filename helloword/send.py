import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='vickymsgque')

channel.basic_publish(exchange='', routing_key='msg', body='Hello World!')
print(" [x] Sent 'hi vicky'")
connection.close()