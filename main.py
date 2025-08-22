from fastapi import FastAPI

app = FastAPI(title="Gestor de Fundo de Impacto")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Gestor de Fundo de Impacto"}