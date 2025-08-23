from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.investment import InvestmentResponse, InvestmentCreate
import repositories.investment as repository
from database.connection import get_db_session

router = APIRouter()

@router.post("/investments", status_code=201, response_model=InvestmentResponse)
async def create_investment(
    investment_data: InvestmentCreate,
    db: AsyncSession = Depends(get_db_session)
):
    """
    Recebe os dados de um investimento, salva no banco de dados
    e retorna o registro criado.
    """
    new_investment = await repository.create_investment(
        db=db,
        investment_data=investment_data
    )
    return new_investment