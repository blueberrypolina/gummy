from dataclasses import dataclass
from datetime import datetime


@dataclass
class Master:
    master_id: int
    rating: float
    address: str
