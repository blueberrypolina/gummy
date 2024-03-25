from datetime import datetime
from client import Client
from service import Service
from dataclasses import dataclass


@dataclass
class Appointment:
    client: Client
    service: Service
    appointment_time: datetime
