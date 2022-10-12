import sqlite3


connect_to_db = sqlite3.connect(
    input(str('Insira o caminho para a base de dados local: ')))

cur = connect_to_db.cursor()

################################################
cur.execute("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;")
################################################

listrows = cur.fetchall()
for x in listrows:
    print(x)


cur.close()

connect_to_db.commit()

connect_to_db.close()
