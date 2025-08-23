import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from database.connection import async_engine
from models.investment import Base



async def create_db_tables():
    """
    Função assíncrona para criar as tabelas no banco de dados
    com base nos modelos definidos que herdam de Base.
    """
    async with async_engine.begin() as conn:
        print("Iniciando a criação das tabelas...")
        await conn.run_sync(Base.metadata.create_all)
        print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    asyncio.run(create_db_tables())