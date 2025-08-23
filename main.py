from fastapi import FastAPI
from routers import investment

app = FastAPI(title="Gestor de Fundo de Impacto")

app.include_router(
    investment.router,
    prefix="/api/v1",
    tags=["Investments"]
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Gestor de Fundo de Impacto"}