import sqlite3
import time

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
cur.execute("DROP TABLE IF EXISTS nome_da_tabela")
######################################################



cur.execute("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;")
listrows = cur.fetchall()
for x in listrows:
    print(x)

connect_to_db.commit()

cur.close()

connect_to_db.close()
