import sqlite3

from OOP.fox_classes import Encomendas

connect_to_db = sqlite3.connect(
    input(str("database path(include extensions): ")))

cur = connect_to_db.cursor()

################################################
encomenda = Encomendas(1, 2, 5, 10, 'Em Trânsito', '16/11/2020')
################################################
cur.execute('''INSERT INTO Encomendas VALUES 
            (NULL, :id_artigo, :id_cliente, :quantidade, 
                    :valor, :estado, :data_registo)''',
            {'id_artigo': encomenda.id_artigo, 'id_cliente': encomenda.id_cliente, 'quantidade': encomenda.quantidade,
             'valor': encomenda.valor, 'estado': encomenda.estado, 'data_registo': encomenda.data_registo})
################################################

cur.execute('''SELECT * FROM Encomendas WHERE 
            id_artigo = :id_artigo AND id_cliente = :id_cliente AND data_registo = :data_registo''',
            {'id_artigo': encomenda.id_artigo, 'id_cliente': encomenda.id_cliente,
             'data_registo': encomenda.data_registo, })
print(cur.fetchone())

connect_to_db.commit()

cur.close()

connect_to_db.close()
