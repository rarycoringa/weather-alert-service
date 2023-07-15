import logging
import os

import pika as pk

from subscriber.callbacks import callback
from subscriber.models import AlertQueue

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    broker_user = os.environ.get("RABBITMQ_USER", "guest")
    broker_pass = os.environ.get("RABBITMQ_PASS", "guest")
    broker_host = os.environ.get("RABBITMQ_HOST", "localhost")
    broker_port = os.environ.get("RABBITMQ_PORT", "5672")
    broker_vhost = os.environ.get("RABBITMQ_VHOST", "/")

    broker_connection = pk.BlockingConnection(pk.URLParameters(f"amqp://{broker_user}:{broker_pass}@{broker_host}:{broker_port}/{broker_vhost}"))

    broker_channel = broker_connection.channel()

    for queue in list(AlertQueue):
        queue_name = queue.value
        broker_channel.queue_declare(queue=queue_name)
        broker_channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    broker_channel.start_consuming()
    
    broker_connection.close()
