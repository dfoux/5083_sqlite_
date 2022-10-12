import sqlite3


connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
nome_completo = 'Diogo Oliveira'
######################################################
cur.execute('''SELECT * FROM Clientes WHERE 
nome_completo=:nome_completo''', {'nome_completo': nome_completo,})

print(cur.fetchone())
######################################################

cur.close()

connect_to_db.close()