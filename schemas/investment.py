import uuid
from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class InvestmentCreate(BaseModel):
    company_name: str
    amount: Decimal
    investment_date: date
    next_report_date: date

class InvestmentResponse(InvestmentCreate):
    id: int
    uuid: uuid.UUID

    class Config:
        from_attributes = True