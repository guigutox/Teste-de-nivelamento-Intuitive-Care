from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

# Carregar dados do CSV
df = pd.read_csv("Data/Relatorio_cadop.csv", sep=";", encoding="UTF-8")

@app.get("/buscar")
def buscar_operadoras(ddd: int = Query(..., description="Informe o DDD")):
    # Certifique-se de que a coluna está sendo referenciada corretamente
    resultados = df[df["DDD"] == ddd]  # Alterado para "DDD"
    return resultados[["Razao_Social", "CNPJ", "Logradouro"]].to_dict(orient="records") # Certifique-se do nome correto da coluna

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
