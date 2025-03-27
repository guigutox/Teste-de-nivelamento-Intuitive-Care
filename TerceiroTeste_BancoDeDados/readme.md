# Teste de Banco de dados

Criar scripts SQL para executar as tarefas

## 📋 Pré-requisitos
- Postgres > 10


## ⚠️AVISO⚠️

Para a realização dessa tarefa foram necessárias modificações e a exclusão de um dos trimestres para que houvesse pleno funcionamento, além da inclusão do realatorio_cadop_canceladas.csv que adiciona as operadoras que foram canceladas.

- A razão pela qual foi incluido é que todos os trimestres tinham empresas as quais não estavam constatadas no relatorio_cadop, então causava uma inconsistência nos dados para realização dos testes, por isso foi necessário inserir o relatório das canceladas que adicionavam todas as necessárias para funcionamento e realização da atividade.

- Foi necessário formatar em todos os trimestres os valores monetários, pois estava causando problemas por estarem separados com "," e não com "."

- Foi necessário ignorar o 4T2023, pois possui mais de 20 mil linhas inconsistentes, pois utilizavam REG_ANS inexistentes o que causa um problema na realização do do teste e durante a inserção por conta da relação entre as tabelas de operadoras e a tabela demonstracoes contabeis.


## 🚀 Como usar

1. Extraia o arquivo Data.zip

2. Utilize os comandos de create table para criar as tabelas no postgres

3. Para inserir as informações será necessário utilizar o PSQL e inserir por ele, por questões de problemas de autorização de leitura pelo postgres a partir de um pgadmin, por exemplo.

4. Abra o CMD e utilize o seguinte comando substituindo os campos usuario e database pelo seu usuario e database:
```
psql -U usuario -d nome_do_banco
```

5. Nesse passo serão inseridas as operadoras.No terminal PSQL, cole o primeiro caminho e substitua o X pelo caminho dos arquivos no primeiro substitua pelo caminho do arquivo Relatorio_cadop.csv, após isso repita o processo para o segundo e  substitua o X pelo caminho do Relatorio_cadop_canceladas.csv

```
\COPY operadoras_ativas ( Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade,Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP,DDD, Telefone, Fax, Email, Representante,Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) FROM 'X' WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');


\COPY operadoras_ativas FROM 'X' DELIMITER ';' CSV HEADER ENCODING 'UTF8'

```


5. Agora para inserir os dados trimestrais, ainda no terminal PSQL Substitua o X para com o caminho dentro da pasta data para cada trimestre, assim como está no script.sql com excessão do 4T2023 (explicação na sessão aviso)

```
\COPY demonstracoes_contabeis FROM 'X' DELIMITER ';' CSV HEADER ENCODING 'UTF8'

---EXEMPLO: 
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'

```

6. Agora basta realizar as buscas que estão indicadas ao fim do script.


