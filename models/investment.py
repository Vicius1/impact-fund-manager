import uuid
from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__ = "investments"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(PG_UUID(as_uuid=True), default=uuid.uuid4, nullable=False, index=True, unique=True)
    company_name = Column(String, nullable=False, index=True)
    amount = Column(Numeric(10, 2), nullable=False)
    investment_date = Column(Date, nullable=False)
    next_report_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Investment(id={self.id}, company_name='{self.company_name}')>"