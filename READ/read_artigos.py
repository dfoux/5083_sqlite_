import sqlite3


connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
nome = 'Laranja'
######################################################
cur.execute('''SELECT * FROM Artigos WHERE 
nome=:nome''', {'nome': nome,})

print(cur.fetchone())
######################################################

cur.close()

connect_to_db.close()
