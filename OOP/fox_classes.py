class Artigos:
    def __init__(self, nome, id_fornecedor, preco, stock, data_registo):
        self.nome = nome
        self.id_fornecedor = id_fornecedor
        self.preco = preco
        self.stock = stock
        self.data_registo = data_registo

    def __repr__(self):
        return f"Artigos('{self.nome} {self.id_fornecedor} {self.stock}'"


class Clientes:

    def __init__(self, nome_completo, telefone, email, localidade, data_registo):
        self.nome_completo = nome_completo
        self.telefone = telefone
        self.email = email
        self.localidade = localidade
        self.data_registo = data_registo

    def __repr__(self):
        return f"Clientes('{self.nome_completo} {self.telefone} {self.email}'"


class Encomendas:
    def __init__(self, id_artigo, id_cliente, quantidade, valor, estado, data_registo):
        self.id_artigo = id_artigo
        self.id_cliente = id_cliente
        self.quantidade = quantidade
        self.valor = valor
        self.estado = estado
        self.data_registo = data_registo

    def __repr__(self):
        return f"Encomendas('{self.id_artigo} {self.id_cliente} {self.estado}'"


class Fornecedores:
    def __init__(self, nome, telefone, data_registo):
        self.nome = nome
        self.telefone = telefone
        self.data_registo = data_registo

    def __repr__(self):
        return f"Fornecedores('{self.nome} {self.telefone}'"
