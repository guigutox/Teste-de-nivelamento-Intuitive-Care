# Teste de Transformação de dados

Script Python para extrair os dados do anexo 1 obtido no primeiro teste, passar para um csv e compactar em zip

## 📋 Pré-requisitos
- Python 3.0+
- Bibliotecas listadas em `requirements.txt`

## 🛠 Instalação


1. Criar ambiente virtual:

    **Caso o SO seja WINDOWS:**
    ```bash
    python3 -m venv venv
    ```
    Em seguida use:
    ```bash
    venv\Scripts\activate
    ```


    Em caso de problemas de segurança do Powershell, execute o powershell como administrador e digite o comando: 
    ```
    Set-ExecutionPolicy RemoteSigned
    ```

    Depois, tente criar o VENV novamente.

    **Caso o SO seja LINUX:**
    ``` bash
    python3 -m venv venv

    chmod +x ./venv/bin/activate

    source venv/bin/activate
    ```


2. Instale as dependências:

    ```bash 
    pip install -r requirements.txt
    ```

## 🚀 Como usar

Use o seguitne comando no console:
```bash
python main.py
```



