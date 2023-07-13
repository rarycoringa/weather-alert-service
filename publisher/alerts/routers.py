from typing import NoReturn

from fastapi import APIRouter
from fastapi.responses import Response

from publisher.alerts.schemas import AlertSchema

import pika

router_prefix: str = "/alerts"

router_tag: str = "ALERTS"

router: APIRouter = APIRouter(
    prefix=router_prefix,
    tags=[router_tag],
)

@router.post(
    path="",
    response_model=None,
    status_code=202,
    summary="Create Alert",
    description="Create an alert to be delivered to all subscribed receivers.",
    response_description="Accepted",
    response_class=Response,
)

def create_alert(alert: AlertSchema) -> NoReturn:
    # Connecting with RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Creating RabbitMQ exchange
    channel.exchange_declare(exchange='weather_alert_exchange', exchange_type='direct')

    channel.queue_declare(queue='YELLOW')
    channel.queue_declare(queue='ORANGE')
    channel.queue_declare(queue='RED')

    channel.basic_publish(exchange='weather_alert_exchange',
                      routing_key=alert.type,
                      body='Publishing alert of type ' + alert.type)

    connection.close()