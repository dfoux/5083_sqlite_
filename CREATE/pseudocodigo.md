Pseudocódigo:

Criação de bases de dados:

Primeiro passo:

Se a tabela Artigos existir:
deitar fora a tabela;

Criar tabela Artigos (
    identificação - número inteiro - Chave primária
)



DROP TABLE IF EXISTS Artigos; 
DROP TABLE IF EXISTS Encomendas; 
DROP TABLE IF EXISTS Clientes ; 
DROP TABLE IF EXISTS Fornecedores;
DROP TABLE IF EXISTS Aux;

CREATE TABLE Artigos (
    id  INTEGER PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    id_fornecedor INTEGER NOT NULL, 
    preco REAL,
    stock INTEGER,
    data_registo VARCHAR(10) NOT NULL,
    UNIQUE (nome, id_fornecedor) ON CONFLICT IGNORE,
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedores (id)    
);
