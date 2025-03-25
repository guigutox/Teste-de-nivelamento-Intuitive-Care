import os
import requests
from bs4 import BeautifulSoup
import zipfile


def baixar_anexos():

    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    pasta = "anexos"
    zip_nome = "anexos_compactados.zip"

    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", string=lambda text: text and 'Anexo' in text) 
        
        pdf_links = []

        for link in links:
            href = link["href"]
            if href.endswith(".pdf"):
                pdf_links.append(href)

        anexo_i_url = pdf_links[0] 
        anexo_ii_url = pdf_links[1]

        
        print(f"Link do Anexo I encontrado: {anexo_i_url}")
        print(f"Link do Anexo II encontrado: {anexo_ii_url}")


        arquivos_baixados = []
        nomes_arquivos = ["Anexo_I.pdf", "Anexo_II.pdf"]
        
        for url_pdf, nome_arquivo in zip(pdf_links[:2], nomes_arquivos):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            
            print(f"\nBaixando {url_pdf}...")
            response_pdf = requests.get(url_pdf, stream=True)
            response_pdf.raise_for_status()
            
            with open(caminho_arquivo, 'wb') as f:
                for chunk in response_pdf.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Salvo como: {caminho_arquivo}")
            arquivos_baixados.append(caminho_arquivo)
        
        print(f"\nCriando arquivo compactado: {zip_nome}")
        with zipfile.ZipFile(zip_nome, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for arquivo in arquivos_baixados:
                zipf.write(arquivo, os.path.basename(arquivo))
                print(f"Adicionado ao ZIP: {os.path.basename(arquivo)}")

        print("\nProcesso concluído com sucesso!")
        print(f"Arquivos salvos em: {os.path.abspath(pasta)}")
        print(f"Arquivo ZIP criado: {os.path.abspath(zip_nome)}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    baixar_anexos()