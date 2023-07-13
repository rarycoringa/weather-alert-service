from typing import NoReturn
import pika

def callback() -> NoReturn:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    #channel.exchange_declare(exchange='logs', exchange_type='fanout')

    channel.queue_declare(queue='YELLOW')
    channel.queue_declare(queue='ORANGE')
    channel.queue_declare(queue='RED')

    # Set up a consumer for each queue
    channel.basic_consume(queue='YELLOW', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='ORANGE', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='RED', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()