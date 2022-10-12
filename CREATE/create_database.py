import sqlite3
import time

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

################################################
cur.executescript('''
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
CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY,
    nome_completo VARCHAR(50) NOT NULL,
    telefone VARCHAR(50),
    email VARCHAR(50),
    localidade VARCHAR(50),
    data_registo VARCHAR(50) NOT NULL,
    UNIQUE (nome_completo, telefone, email, localidade, data_registo) ON CONFLICT IGNORE    
);  
CREATE TABLE Encomendas (
    id INTEGER PRIMARY KEY,    
    id_artigo INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor REAL NOT NULL,
    estado VARCHAR(20) NOT NULL,
    data_registo VARCHAR(10) NOT NULL,
    UNIQUE (id_artigo, id_cliente, data_registo) ON CONFLICT IGNORE,
    FOREIGN KEY (id_artigo) REFERENCES Artigos (id),    
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id)
);
CREATE TABLE Fornecedores (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(30) NOT NULL UNIQUE,
    telefone VARCHAR(10),
    data_registo VARCHAR(10) NOT NULL,
    UNIQUE (nome) ON CONFLICT IGNORE    
);  
CREATE TABLE Aux (
    id  NULL
);''')
################################################

print("Creating table Artigos.")
time.sleep(0.7)
print("Creating table Clientes.")
time.sleep(0.7)
print("Creating table Encomendas.")
time.sleep(0.7)
print("Creating table Fornecedores.")
time.sleep(0.7)
print("Creating Aux table.")
time.sleep(0.7)
print("Database created!")

cur.execute("SELECT * FROM sqlite_master;")
listrows = cur.fetchall()
for x in listrows:
    print(x)
    time.sleep(0.7)

cur.close()

connect_to_db.commit()

connect_to_db.close()
