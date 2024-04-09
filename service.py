from dataclasses import dataclass

@dataclass(frozen=True)
class Service:
    id: int
    name: str
    payment: str
    cost: float
