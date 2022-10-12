import sqlite3

from OOP.fox_classes import Fornecedores

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

################################################
fornecedor = Fornecedores('Joaquim das Couves', '916969696', '16/11/2020')
################################################
cur.execute('''INSERT INTO Fornecedores VALUES 
            (NULL, :nome, :telefone, :data_registo)''',
            {'nome': fornecedor.nome, 'telefone': fornecedor.telefone, 'data_registo': fornecedor.data_registo})
################################################

cur.execute('''SELECT * FROM Fornecedores WHERE 
nome=:nome''', {'nome': fornecedor.nome, })
print(cur.fetchone())


connect_to_db.commit()

cur.close()

connect_to_db.close()
