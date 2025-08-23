from sqlalchemy.ext.asyncio import AsyncSession

import models.investment as models
import schemas.investment as schemas

async def create_investment(
    db: AsyncSession,
    investment_data: schemas.InvestmentCreate
) -> models.Investment:
    """
    Cria um novo registro de investimento no banco de dados.
    """
    data = investment_data.model_dump()

    db_investment = models.Investment(**data)

    db.add(db_investment)

    await db.commit()

    await db.refresh(db_investment)

    return db_investment