import sqlite3


connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()


######################################################
nome = 'Abacate'
preco = 0,5
id_fornecedor = 5
stock = 50
######################################################


cur.execute('''UPDATE Artigos SET 
preco = :preco WHERE nome = :nome''', {'nome': nome, 'preco': preco})


cur.execute('''SELECT * FROM Artigos WHERE 
nome=:nome''', {'nome': nome,})
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()