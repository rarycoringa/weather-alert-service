from typing import NoReturn

from fastapi import APIRouter
from fastapi.responses import Response

from publisher.alerts.schemas import AlertSchema

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
    # the publishing in queues must be done here
    pass