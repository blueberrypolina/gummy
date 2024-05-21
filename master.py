from dataclasses import dataclass
from datetime import datetime


@dataclass
class Master:
    id: int
    rating: float
    address: str
