from enum import Enum

from pydantic import BaseModel

class AlertType(str, Enum):
    YELLOW: str = "YELLOW"
    ORANGE: str = "ORANGE"
    RED: str = "RED"

class AlertSchema(BaseModel):
    type: AlertType
    title: str
    description: str
    source_agency: str
