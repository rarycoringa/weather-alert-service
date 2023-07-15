from enum import Enum

from pydantic import BaseModel

class AlertType(str, Enum):
    BLUE: str = "BLUE"
    YELLOW: str = "YELLOW"
    ORANGE: str = "ORANGE"
    RED: str = "RED"

class CategoryType(str, Enum):
    FOREST_FIRE: str = "FOREST_FIRE"
    SNOW_STORM: str = "SNOW_STORM"
    THUNDERSTORM: str = "THUNDERSTORM"
    HURRICANE: str = "HURRICANE"
    TORNADO: str = "TORNADO"

class Alert(BaseModel):
    type: AlertType
    category: CategoryType
    title: str
    description: str
    source_agency: str
