from enum import Enum

class AlertQueue(str, Enum):
    blue: str = "blue"
    yellow: str = "yellow"
    orange: str = "orange"
    red: str = "red"