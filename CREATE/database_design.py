import sqlite3


connect_to_db = sqlite3.connect(
    input(str('Insira o caminho para a base de dados local: ')))

cur = connect_to_db.cursor()

################################################
# cur.execute('''
# SELECT * FROM sqlite_master WHERE type='table';''')
# cur.execute('''
# SELECT * FROM sqlite_schema;''')
cur.execute('''PRAGMA table_info(Artigos);''')



################################################

listrows = cur.fetchall()
for x in listrows:
    print(x)
    for y in x:
        print(y)


cur.close()

connect_to_db.commit()

connect_to_db.close()
