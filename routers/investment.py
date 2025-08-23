from fastapi import APIRouter
from schemas.investment import InvestmentCreate

router = APIRouter()

@router.post("/investments", status_code=201)
def create_investment(investment: InvestmentCreate):
    """
    Recebe um investimento e apenas retorna para confirmar o recebimento.
    """
    print(f"Investimento recebido: {investment.company_name}")
    return {"message": "Investimento recebido com sucesso", "data": investment}