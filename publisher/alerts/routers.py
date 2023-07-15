import os

from typing import Dict
from typing import NoReturn

import pika as pk

from fastapi import APIRouter
from fastapi.responses import Response

from publisher.alerts.models import Alert
from publisher.alerts.models import AlertType

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
    description="Create an alert to be published for all subscribers.",
    response_description="Accepted",
    response_class=Response,
)
def create_alert(alert: Alert) -> NoReturn:

    broker_user = os.environ.get("RABBITMQ_USER", "guest")
    broker_pass = os.environ.get("RABBITMQ_PASS", "guest")
    broker_host = os.environ.get("RABBITMQ_HOST", "localhost")
    broker_port = os.environ.get("RABBITMQ_PORT", "5672")
    broker_vhost = os.environ.get("RABBITMQ_VHOST", "/")

    broker_connection = pk.BlockingConnection(pk.URLParameters(f"amqp://{broker_user}:{broker_pass}@{broker_host}:{broker_port}/{broker_vhost}"))

    broker_channel = broker_connection.channel()

    queue_name = alert.type.value.lower()

    broker_channel.queue_declare(queue=queue_name)
    broker_channel.basic_publish(exchange="", routing_key=queue_name, body=alert.json())

    broker_connection.close()
    
