import sqlite3

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
nome = 'Pera'
preco = 1.6
id_fornecedor = 5
stock = 90
######################################################
cur.execute('''UPDATE Artigos SET 
preco = :preco, id_fornecedor = :id_fornecedor, 
stock = :stock WHERE nome = :nome''',
{'nome': nome, 'preco': preco, 'id_fornecedor': id_fornecedor, 'stock': stock})
######################################################

cur.execute('''SELECT * FROM Artigos WHERE 
nome=:nome''', {'nome': nome, })
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()
