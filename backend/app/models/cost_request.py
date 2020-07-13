from sqlalchemy import (
    Column, Integer, String,
    Float, Date, DateTime,
    DECIMAL, Boolean
)
from sqlalchemy.sql import func

from db.base_class import Base


class CostRequest(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    cargo_type = Column(String)
    declared_value = Column(Float)
    calculated_value = Column(DECIMAL, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    succeed = Column(Boolean, default=True)
