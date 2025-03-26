CREATE TABLE operadoras_ativas (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao INTEGER,
    data_registro_ans DATE,
	Data_Descredenciamento DATE,
    Motivo_do_Descredenciamento VARCHAR(255)
);

CREATE TABLE demonstracoes_contabeis (
    data DATE,
    registro_ans VARCHAR(20),
    conta_contabil VARCHAR(100),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras_ativas(registro_ans)
);



-- DESCONSIDERADA, Explicação no reade.md
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\4T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
 

-- Inserir Operadoras
\COPY operadoras_ativas ( Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade,Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP,DDD, Telefone, Fax, Email, Representante,Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\Relatorio_cadop.csv' WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');
\COPY operadoras_ativas FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\Relatorio_cadop_canceladas.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'



-- Inserir Demonstracoes Contabeis
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\2T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
\COPY demonstracoes_contabeis FROM 'D:\Projetos\Teste-de-nivelamento-Intuitive-Care\TerceiroTeste_BancoDeDados\Data\4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'



--QUERYS 

-- 3.3 Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

SELECT 
    o.razao_social,
    o.nome_fantasia,
    o.uf,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE 
    (d.descricao ILIKE '%Despesas com Eventos / Sinistros%' OR
     d.descricao ILIKE '%AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%' OR
     d.descricao ILIKE '%EVENTOS/SINISTROS CONHECIDOS%')
    AND d.data >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '3 months'
    AND d.data < DATE_TRUNC('quarter', CURRENT_DATE)
GROUP BY 
    o.razao_social, o.nome_fantasia, o.uf
HAVING 
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) > 0
ORDER BY 
    total_despesas DESC
LIMIT 10;


-- 3.4 Quais as 10 operadoras com maiores despesas nessa categoria no último ano? 
SELECT 
    o.razao_social,
    o.nome_fantasia,
    o.uf,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas_anual
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE 
    (d.descricao ILIKE '%Despesas com Eventos / Sinistros%' OR
     d.descricao ILIKE '%AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%' OR
     d.descricao ILIKE '%EVENTOS/SINISTROS CONHECIDOS%')
    AND d.data >= DATE_TRUNC('year', CURRENT_DATE) - INTERVAL '1 year'
    AND d.data < DATE_TRUNC('year', CURRENT_DATE)
GROUP BY 
    o.razao_social, o.nome_fantasia, o.uf
HAVING 
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) > 0
ORDER BY 
    total_despesas_anual DESC
LIMIT 10;