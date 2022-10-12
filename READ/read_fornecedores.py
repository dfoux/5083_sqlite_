import sqlite3


connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
nome = 'Joaquim das Couves'
######################################################

cur.execute('''SELECT * FROM Fornecedores WHERE 
nome=:nome''', {'nome': nome, })

print(cur.fetchone())
######################################################

cur.close()

connect_to_db.close()