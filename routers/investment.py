from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.investment import InvestmentResponse, InvestmentCreate
import services.investment as investment_service
import repositories.investment as repository
from database.connection import get_db_session

router = APIRouter()

@router.post("/investments", status_code=201, response_model=InvestmentResponse)
async def create_investment(
    investment_data: InvestmentCreate,
    db: AsyncSession = Depends(get_db_session)
):
    """
    Endpoint para criar um novo investimento.
    Apenas recebe a requisição e a delega para a camada de serviço.
    """
    created_investment = await investment_service.create_new_investment_flow(
        db=db,
        investment_data=investment_data
    )
    return created_investment

@router.get("/investments", response_model=list[InvestmentResponse])
async def list_investments(
    db: AsyncSession = Depends(get_db_session)
):
    """
    Retorna todos os registros de investimento.
    """
    investments = await repository.get_all_investments(db=db)
    return investments