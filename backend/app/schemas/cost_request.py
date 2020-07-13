from datetime import date
from pydantic import BaseModel


class CostRequest(BaseModel):
    date: date
    cargo_type: str
    declared_value: float = 100
