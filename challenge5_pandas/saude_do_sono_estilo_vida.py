import pandas as pd
import numpy as np


df = pd.read_csv('saude_do_sono_estilo_vida.csv')

# Renomeação das colunas conforme solicitado
df.rename(columns={
    'ID': 'Identificador',
    'Pressão sanguíneaaaa': 'Pressão_Sanguínea', 
    'Ocupação': 'Profissão',
    'Categoria BMI': 'Categoria_IMC'
}, inplace=True)

# Verificação dos nomes das colunas
print("Nomes das colunas no DataFrame:\n", df.columns)

# Função para processar e converter os valores da pressão sanguínea
def processar_pressao_sanguinea(val):
    try:
        sistolica, diastolica = map(float, val.split('/'))
        return (sistolica + diastolica) / 2
    except Exception as e:
        print(f"Erro ao processar a pressão sanguínea '{val}': {e}")
        return np.nan

# Aplicando a função na coluna 'Pressão_Sanguínea'
df['Pressão_Sanguínea'] = df['Pressão_Sanguínea'].apply(processar_pressao_sanguinea)

# 2. Média, moda e mediana de horas de sono para cada profissão
media_sono = df.groupby('Profissão')['Duração do sono'].mean()
moda_sono = df.groupby('Profissão')['Duração do sono'].agg(pd.Series.mode)
mediana_sono = df.groupby('Profissão')['Duração do sono'].median()

print("Média de duração do sono por profissão:\n", media_sono)
print("\nModa de duração do sono por profissão:\n", moda_sono)
print("\nMediana de duração do sono por profissão:\n", mediana_sono)

# 3. Porcentagem de obesos entre engenheiros de software
engenheiros_software = df[df['Profissão'] == 'Engenheiro de Software']
if engenheiros_software.shape[0] > 0:
    porcentagem_obesos = (engenheiros_software[engenheiros_software['Categoria_IMC'] == 'Obeso'].shape[0] / engenheiros_software.shape[0]) * 100
else:
    porcentagem_obesos = 0
print(f"Porcentagem de obesos entre engenheiros de software: {porcentagem_obesos:.2f}%")

# 4. Advogados e representantes de vendas - média de horas de sono
adv_vendas = df[df['Profissão'].isin(['Advogado(a)', 'Representante de Vendas'])]
media_sono_adv_vendas = adv_vendas.groupby('Profissão')['Duração do sono'].mean()
print("Média de duração do sono para Advogados e Representantes de Vendas:\n", media_sono_adv_vendas)

# 5. Enfermagem e Medicina - média de horas de sono
enf_med = df[df['Profissão'].isin(['Enfermeiro(a)', 'Médico(a)'])]
media_sono_enf_med = enf_med.groupby('Profissão')['Duração do sono'].mean()
print("Média de duração do sono para Enfermeiros e Médicos:\n", media_sono_enf_med)

# 6. Subconjunto de colunas selecionadas
subconjunto = df[['Identificador', 'Gênero', 'Idade', 'Pressão_Sanguínea', 'Frequência cardíaca']]
print(subconjunto.head())

# 7. Profissão menos frequente
profissao_menos_frequente = df['Profissão'].value_counts().idxmin()
print(f"A profissão menos frequente é: {profissao_menos_frequente}")

# 8. Média da pressão sanguínea por gênero
media_pressao_genero = df.groupby('Gênero')['Pressão_Sanguínea'].mean()
print("Média da pressão sanguínea por gênero:\n", media_pressao_genero)

# 9. Moda da duração do sono
moda_sono_geral = df['Duração do sono'].mode()[0]
print(f"A moda da duração do sono é: {moda_sono_geral} horas")

# 10. Comparação de passos diários com base na frequência cardíaca
acima_70 = df[df['Frequência cardíaca'] > 70]
abaixo_ou_igual_70 = df[df['Frequência cardíaca'] <= 70]
media_passos_acima_70 = acima_70['Passos diários'].mean()
media_passos_abaixo_ou_igual_70 = abaixo_ou_igual_70['Passos diários'].mean()
print(f"Média de passos para frequência cardíaca acima de 70: {media_passos_acima_70}")
print(f"Média de passos para frequência cardíaca menor ou igual a 70: {media_passos_abaixo_ou_igual_70}")

