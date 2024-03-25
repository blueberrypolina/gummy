from dataclasses import dataclass

@dataclass(frozen=True)
class Service:
    service_id: int
    name: str
    payment: str
    cost: float
