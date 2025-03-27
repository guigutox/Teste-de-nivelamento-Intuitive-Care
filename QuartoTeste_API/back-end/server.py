from fastapi import FastAPI, Query
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("Data/Relatorio_cadop.csv", sep=";", encoding="UTF-8")

@app.get("/buscar")
def buscar_operadoras(termo_busca: str = Query(..., description="Informe o termo de busca")):
    cols = [
        "Razao_Social", "CNPJ", "Nome_Fantasia", "Modalidade", "Logradouro", 
        "Numero", "Complemento", "Bairro", "Cidade", "UF", "CEP", "DDD", 
        "Telefone", "Fax", "Endereco_eletronico", "Representante", 
        "Cargo_Representante", "Regiao_de_Comercializacao", "Data_Registro_ANS"
    ]
    
    df[cols] = df[cols].astype(str)
    
    resultados = df.copy()
    
    resultados['relevancia'] = 0
    
    pesos = {
        "CNPJ": 30,          

        "Razao_Social": 25,   
        "Nome_Fantasia": 20, 
        "Cidade": 15,
        "UF": 12,
        "Regiao_de_Comercializacao": 10,
        "Logradouro": 8,
        "Bairro": 6,
        "CEP": 5,
        "Telefone": 7,
        "Endereco_eletronico": 6,
        "DDD": 4,
        "Fax": 3,
        "Representante": 5,
        "Cargo_Representante": 2,
        "Modalidade": 4,
        "Complemento": 3,
        "Numero": 2,
        "Data_Registro_ANS": 1
    }
    
    BONUS_EXATO = 10

    resultados['relevancia'] = 0

    for col in cols:
        weight = pesos.get(col, 1)
        
        mask_parcial = resultados[col].str.contains(termo_busca, case=False, na=False)
        resultados.loc[mask_parcial, 'relevancia'] += weight
        
        mask_exato = resultados[col].str.lower() == termo_busca.lower()
        resultados.loc[mask_exato, 'relevancia'] += BONUS_EXATO

    resultados = resultados[resultados['relevancia'] > 0]
    resultados = resultados.sort_values('relevancia', ascending=False)
    
    return resultados.to_dict(orient="records")
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
