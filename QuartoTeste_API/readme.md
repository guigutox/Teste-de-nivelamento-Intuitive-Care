# Teste de API

Script python para realizar buscas no CSV e retornar a part

## Collection de teste do postman
A collection se encontra na pasta raiz do projeto, o arquivo tem o nome: Coleção Teste 4.postman_collection
Basta baixa-lo e importar no postman.

## 📋 Pré-requisitos
- Python 3.0+
- Node

## 🛠 Instalação back-end
1. Entre na pasta back-end

2. Criar ambiente virtual:

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


3. Instale as dependências:

    ```bash 
    pip install -r requirements.txt
    ```

## 🛠 Instalação front-end:

1. Entre na pasta front-end

2.  Para baixar dependencias utilize no terminal:
    ```
    npm install
    ```

3. Para rodar o projeto utilize no terminal:
    ```
    npm run serve
    ```



## 🚀 Como usar

1- Use o seguinte comando com o terminal na pasta back-end para subir o back:
    ```bash
    python main.py
    ```

2-  Use o seguinte comando com terminal na pasta front-end para subir o front:
    ```
    npm run serve
    ```





