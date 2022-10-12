import sqlite3

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

######################################################
id = 1

######################################################
cur.execute("DELETE FROM Encomendas WHERE id = :id", {'id': id})
######################################################

cur.execute("SELECT * FROM Encomendas WHERE id = :id", {'id': id, })

cur.execute("SELECT * FROM Encomendas WHERE id = :id", {'id': id, })
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()
