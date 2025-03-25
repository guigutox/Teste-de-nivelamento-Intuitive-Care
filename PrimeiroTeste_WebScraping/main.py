import os
import requests
from bs4 import BeautifulSoup


def baixar_anexos():

    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    pasta = "anexos"

    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", string=lambda text: text and 'Anexo' in text) 
        for link in links:
            print(link["href"])

        pdf_links = []

        for link in links:
            href = link["href"].lower()
            if href.endswith(".pdf"):
                pdf_links.append(href)
            
        
        print(f"Quantidade de links encontrados: {len(pdf_links)}")
        anexo_i_url = pdf_links[0] 
        anexo_ii_url = pdf_links[1]

        
        print(f"Link do Anexo I encontrado: {anexo_i_url}")
        print(f"Link do Anexo II encontrado: {anexo_ii_url}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")


if __name__ == "__main__":
    baixar_anexos()