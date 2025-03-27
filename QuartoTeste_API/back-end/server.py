from fastapi import FastAPI, Query
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (troque conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("Data/Relatorio_cadop.csv", sep=";", encoding="UTF-8")

@app.get("/buscar")
def buscar_operadoras(ddd: int = Query(..., description="Informe o DDD")):
    resultados = df[df["DDD"] == ddd]
    return resultados[["Razao_Social", "CNPJ", "Logradouro"]].to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
