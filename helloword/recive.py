import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='127.0.0.1:8000'))
channel = connection.channel()

channel.queue_declare(queue='vickymsgque')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='vickymsgque', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()