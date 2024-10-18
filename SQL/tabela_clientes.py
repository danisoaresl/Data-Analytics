#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.
#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a
#30 anos.
#b) Calcule o saldo médio dos clientes.
#c) Encontre o cliente com o saldo máximo.
#d) Conte quantos clientes têm saldo acima de 1000.
#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#b) Remova um cliente pelo seu ID.


import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('banco_clientes.db')

# Criar um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Apagar a tabela "clientes" se ela já existir
cursor.execute('DROP TABLE IF EXISTS clientes')

# Criar a tabela "clientes"
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo FLOAT NOT NULL
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

# Consultas e Funções Agregadas

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
clientes_maiores_30 = cursor.fetchall()
print("Clientes com idade superior a 30 anos:")
for cliente in clientes_maiores_30:
    print(cliente)

# b) Calcule o saldo médio dos clientes
cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()[0]
print(f"\nSaldo médio dos clientes: {saldo_medio}")

# c) Encontre o cliente com o saldo máximo
cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
cliente_max_saldo = cursor.fetchone()
print(f"\nCliente com saldo máximo: {cliente_max_saldo[0]} com saldo de {cliente_max_saldo[1]}")

# d) Conte quantos clientes têm saldo acima de 1000
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
clientes_acima_1000 = cursor.fetchone()[0]
print(f"\nNúmero de clientes com saldo acima de 1000: {clientes_acima_1000}")

# Atualização e Remoção com Condições

# a) Atualize o saldo de um cliente específico
cursor.execute('''
UPDATE clientes
SET saldo = 5000.00
WHERE id = 2
''')

# b) Remova um cliente pelo seu ID
cursor.execute('''
DELETE FROM clientes
WHERE id = 5
''')

# Commit para salvar as mudanças
conexao.commit()

# Fechar a conexão
conexao.close()
