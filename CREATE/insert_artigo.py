import sqlite3

from OOP.fox_classes import Artigos

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

################################################
artigo = Artigos('Pera', '1', 1.5,
                 '300', '16/11/2020')
################################################
cur.execute('''INSERT INTO Artigos VALUES 
            (NULL, :nome, :id_fornecedor, :preco, 
                    :stock, :data_registo)''',
            {'nome': artigo.nome, 'id_fornecedor': artigo.id_fornecedor, 'preco': artigo.preco,
             'stock': artigo.stock, 'data_registo': artigo.data_registo})
################################################

cur.execute('''SELECT * FROM Artigos WHERE 
nome = :nome''', {'nome': artigo.nome, })

listrows = cur.fetchall()
for x in listrows:
    print(x)


connect_to_db.commit()

cur.close()

connect_to_db.close()
