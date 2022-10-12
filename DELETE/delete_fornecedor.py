import sqlite3

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
id = 1
nome = 'Joaquim das Couves'
######################################################
cur.execute("DELETE from Fornecedores WHERE id = :id AND nome = :nome",
{'id': id, 'nome': nome,})
######################################################

cur.execute("SELECT * FROM Fornecedores WHERE nome=:nome", {'nome': nome, })
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()
