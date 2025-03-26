import pdfplumber
import pandas as pd
import zipfile

pdf_path = "Anexo_I.pdf"


csv_filename = "Rol_Procedimentos.csv"
zip_filename = "Teste_GuilhermeFernandes.zip" 

substituicoes = {
    "OD": "Seg. Odontologica",
    "AMB": "Seg. Ambulatorial",
}

dados = []


with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tabelas = page.extract_table()
        if tabelas:
            for linha in tabelas[1:]:  
                linha_corrigida = [" ".join(celula.split()) if celula else "" for celula in linha]
                dados.append(linha_corrigida)

colunas = ["PROCEDIMENTO", "RN (alteracao)", "VIGENCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPITULO"]
df = pd.DataFrame(dados, columns=colunas)

for col in ["OD", "AMB"]:
    df[col] = df[col].apply(lambda x: substituicoes.get(x, x))  


df.to_csv(csv_filename, index=False, encoding="utf-8", sep=";")

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_filename)

print(f"Arquivo {zip_filename} criado com sucesso!")
