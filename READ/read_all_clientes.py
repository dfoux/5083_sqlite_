import sqlite3

connect_to_db = sqlite3.connect(
    input(str('Insira o caminho para a base de dados local: ')))

cur = connect_to_db.cursor()

cur.execute("SELECT * FROM Clientes;")

listrows = cur.fetchall()
for row in listrows:
        print(row)


cur.close()

connect_to_db.commit()

connect_to_db.close()