from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class InvestmentCreate(BaseModel):
    company_name: str
    amount: Decimal
    investment_date: date
    next_report_date: date