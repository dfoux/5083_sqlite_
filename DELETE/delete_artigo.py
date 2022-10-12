import sqlite3

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
id = 1
nome = 'Abacate'
######################################################
cur.execute("DELETE FROM Artigos WHERE id = :id AND nome = :nome",
            {'id': id, 'nome': nome, })
######################################################

cur.execute('''SELECT * FROM Artigos WHERE 
nome=:nome''', {'nome': nome, })
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()
