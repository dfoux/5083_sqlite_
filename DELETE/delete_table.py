import sqlite3

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
cur.execute("DELETE FROM nome_da_tabela")
######################################################

cur.execute("SELECT * FROM nome_da_tabela;")

listrows = cur.fetchall()
for row in listrows:
    print(row)

connect_to_db.commit()

cur.close()

connect_to_db.close()
