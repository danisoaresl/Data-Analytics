#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.


import sqlite3
import os

# Nome do arquivo do banco de dados
db_file = 'banco_clientes.db'

# Excluir o arquivo do banco de dados se ele já existir
if os.path.exists(db_file):
    os.remove(db_file)

# Conectar ao banco de dados (será criado novamente)
conexao = sqlite3.connect(db_file)

# Criar um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Criar a tabela "clientes"
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo FLOAT NOT NULL
)
''')

# Criar a tabela "compras"
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')

# Inserir alguns registros na tabela "clientes"
cursor.executemany('''
INSERT INTO clientes (id, nome, idade, saldo) 
VALUES (?, ?, ?, ?)
''', [
    (1, 'João Nascimento', 65, 4500.75),
    (2, 'Catarina Terto', 60, 2500.00),
    (3, 'Gustavo Nascimento', 10, 900.50),
    (4, 'Enzo Soares', 20, 6000.00),
    (5, 'Lucas Lima', 28, 999.00)
])

# Inserir algumas compras associadas a clientes existentes na tabela "clientes"
cursor.executemany('''
INSERT INTO compras (cliente_id, produto, valor)
VALUES (?, ?, ?)
''', [
    (1, 'iphone', 6000.00),
    (2, 'ipad', 4000.00),
    (3, 'apple watch', 3000.00),
    (4, 'moto', 50000.00),
    (5, 'mochila', 500.00)
])

# Commit para salvar as mudanças
conexao.commit()

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('''
SELECT clientes.nome, compras.produto, compras.valor
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id
''')

# Mostrar os resultados
compras = cursor.fetchall()
for compra in compras:
    print(compra)

# Fechar a conexão
conexao.close()
