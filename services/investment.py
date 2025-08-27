from sqlalchemy.ext.asyncio import AsyncSession

import repositories.investment as repository
import services.google_drive as google_drive_service
import schemas.investment as schemas
import models.investment as models

async def create_new_investment_flow(
    db: AsyncSession,
    investment_data: schemas.InvestmentCreate
) -> models.Investment:
    """
    O fluxo de negócio para criar um novo investimento.
    Orquestra as chamadas ao banco de dados e a outros serviços.
    """
    new_investment = await repository.create_investment(
        db=db,
        investment_data=investment_data
    )

    if new_investment:
        await google_drive_service.create_folder(
            folder_name=new_investment.company_name
        )

    return new_investment