import sqlite3

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
nome_completo = 'Diogo Delgado'
telefone = '918955499'
email = 'd.o@test.local'
localidade = ''
######################################################
cur.execute('''UPDATE Clientes SET 
nome_completo = :nome_completo, telefone = :telefone, 
email = :email WHERE nome_completo = :nome_completo''',
            {'nome_completo': nome_completo, 'telefone': telefone, 'email': email, 'localidade': localidade})
######################################################

cur.execute('''SELECT * FROM Clientes WHERE 
nome_completo = :nome_completo''', {'nome_completo': nome_completo, })
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()
