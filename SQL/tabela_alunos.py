#Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
#Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas: 
#a) Selecionar todos os registros da tabela "alunos".
#b) Selecionar o nome e a idade dos alunos com mais de 20 anos. 
#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética. 
#d) Contar o número total de alunos na tabela
#Atualização e Remoção 
#a) Atualize a idade de um aluno específico na tabela. 
#b) Remova um aluno pelo seu ID.


import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('banco_alunos.db')

# Criar um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Apagar a tabela "alunos" se ela já existir
cursor.execute('DROP TABLE IF EXISTS alunos')

# Criar a tabela "alunos" novamente
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL
)
''')

# Inserir registros na tabela "alunos"
cursor.executemany('''
INSERT INTO alunos (id, nome, idade, curso) 
VALUES (?, ?, ?, ?)
''', [
    (1, 'João Nascimento', 65, 'Engenharia'),
    (2, 'Catarina Terto', 60, 'Direito'),
    (3, 'Gustavo Nascimento', 10, 'Engenharia'),
    (4, 'Enzo Soares', 20, 'Medicina'),
    (5, 'Lucas Lima', 28, 'Arquitetura')
])

# Consultas Básicas
cursor.execute('SELECT * FROM alunos')
todos_alunos = cursor.fetchall()
print("Todos os registros da tabela 'alunos':")
for aluno in todos_alunos:
    print(aluno)

cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
alunos_maiores = cursor.fetchall()
print("\nAlunos com mais de 20 anos:")
for aluno in alunos_maiores:
    print(aluno)

cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
alunos_engenharia = cursor.fetchall()
print("\nAlunos do curso de Engenharia em ordem alfabética:")
for aluno in alunos_engenharia:
    print(aluno)

cursor.execute('SELECT COUNT(*) FROM alunos')
total_alunos = cursor.fetchone()[0]
print(f"\nNúmero total de alunos: {total_alunos}")

# Atualizar a idade de um aluno específico
cursor.execute('''
UPDATE alunos
SET idade = 23
WHERE id = 1
''')

# Remover um aluno pelo seu ID
cursor.execute('''
DELETE FROM alunos
WHERE id = 5
''')

# Commit para salvar as mudanças
conexao.commit()

# Fechar a conexão
conexao.close()
