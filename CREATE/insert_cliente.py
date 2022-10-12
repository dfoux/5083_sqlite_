import sqlite3

from OOP.fox_classes import Clientes

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

################################################
cliente = Clientes('Diogo Oliveira', '969696969', 'diogo.oliveira@test.local',
                   'Lisboa', '16/11/2020')
################################################
cur.execute('''INSERT INTO Clientes VALUES 
            (NULL, :nome_completo, :telefone, :email, 
                    :localidade, :data_registo)''',
            {'nome_completo': cliente.nome_completo, 'telefone': cliente.telefone, 'email': cliente.email,
             'localidade': cliente.localidade, 'data_registo': cliente.data_registo})
################################################

cur.execute('''SELECT * FROM Clientes WHERE 
nome_completo = :nome_completo''', {'nome_completo': cliente.nome_completo, })
print(cur.fetchone())


connect_to_db.commit()

cur.close()

connect_to_db.close()
