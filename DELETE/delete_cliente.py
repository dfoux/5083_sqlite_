import sqlite3

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
id = 1
nome_completo = 'Diogo Oliveira'
######################################################
cur.execute("DELETE FROM Clientes WHERE id = :id AND nome_completo = :nome_completo",
{'id': id, 'nome_completo': nome_completo,})
######################################################

cur.execute('''SELECT * FROM Clientes WHERE 
nome_completo=:nome_completo''', {'nome_completo': nome_completo, })
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()
