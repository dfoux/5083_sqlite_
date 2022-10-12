import sqlite3

connect_to_db = sqlite3.connect(
    input(str('Insira o caminho para a base de dados local: ')))
cursor = connect_to_db.cursor()


cursor.execute("SELECT * FROM Fornecedores;")
listrows = cursor.fetchall()

for row in listrows:
        print(row)


            
cursor.close()
connect_to_db.commit()
connect_to_db.close()
