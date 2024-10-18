import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Use TkAgg para exibir gráficos em uma janela
matplotlib.use('TkAgg')

# Carregar o arquivo JSON
df = pd.read_json('enem_2023.json')

# Verificar e corrigir nomes de colunas
print("Colunas no DataFrame:", df.columns)
df.rename(columns={'Ciências da natureza': 'Ciências da Natureza'}, inplace=True)

# Verificar se há valores nulos
print("Valores nulos por coluna:")
print(df[['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza']].isnull().sum())

# Remover linhas com valores nulos
df = df.dropna(subset=['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza'])

# Garantir que todas as colunas são numéricas
df[['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza']] = df[['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza']].apply(pd.to_numeric, errors='coerce')

# Recalcular a amplitude
amplitude = df[['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza']].max() - df[['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza']].min()
maior_amplitude = amplitude.idxmax()
print(f"A disciplina com a maior amplitude de nota é: {maior_amplitude}")

# 2. Qual é a média e a mediana para cada uma das disciplinas?
media = df[['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza']].mean()
mediana = df[['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza']].median()

print("\nMédia das disciplinas:")
print(media)
print("\nMediana das disciplinas (sem valores nulos):")
print(mediana)

# 3. Desvio padrão e média ponderados dos 500 estudantes mais bem colocados
df['Nota_Ponderada'] = (df['Redação'] * 2 + df['Matemática'] * 4 + df['Linguagens'] * 2 +
                        df['Ciências humanas'] * 1 + df['Ciências da Natureza'] * 1)

top_500 = df.nlargest(500, 'Nota_Ponderada')
media_ponderada = top_500['Nota_Ponderada'].mean()
desvio_padrao_ponderado = top_500['Nota_Ponderada'].std()

print(f"\nMédia ponderada dos 500 melhores estudantes: {media_ponderada:.2f}")
print(f"Desvio padrão ponderado dos 500 melhores estudantes: {desvio_padrao_ponderado:.2f}")

# 4. Variância e média das notas dos estudantes que entraram no curso de Ciência da Computação (40 vagas)
top_40 = top_500.head(40)
variancia_top_40 = top_40['Nota_Ponderada'].var()
media_top_40 = top_40['Nota_Ponderada'].mean()

print(f"\nMédia das notas dos 40 estudantes que entraram: {media_top_40:.2f}")
print(f"Variância das notas dos 40 estudantes que entraram: {variancia_top_40:.2f}")

# 5. Valor do teto do terceiro quartil para Matemática e Linguagens
terceiro_quartil = df[['Matemática', 'Linguagens']].quantile(0.75)
print("\nTeto do terceiro quartil para Matemática e Linguagens:")
print(terceiro_quartil)

# 6. Histogramas de Redação e Linguagens de 20 em 20 pontos
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(df['Redação'], bins=range(0, 1010, 20), edgecolor='black')
plt.title('Histograma de Redação')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
plt.hist(df['Linguagens'], bins=range(0, 1010, 20), edgecolor='black')
plt.title('Histograma de Linguagens')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()  # Exibir o gráfico diretamente

# Análise de simetria dos histogramas usando skewness
import scipy.stats as stats

# Calcular a assimetria das distribuições
skew_redacao = stats.skew(df['Redação'])
skew_linguagens = stats.skew(df['Linguagens'])

print(f"Assimetria (skewness) da Redação: {skew_redacao:.2f}")
print(f"Assimetria (skewness) da Linguagens: {skew_linguagens:.2f}")

# Analisar a simetria com base nos valores de skewness
if abs(skew_redacao) < 0.5:
    print("O histograma de Redação é aproximadamente simétrico.")
elif skew_redacao > 0:
    print("O histograma de Redação é assimétrico positivo (cauda à direita).")
else:
    print("O histograma de Redação é assimétrico negativo (cauda à esquerda).")

if abs(skew_linguagens) < 0.5:
    print("O histograma de Linguagens é aproximadamente simétrico.")
elif skew_linguagens > 0:
    print("O histograma de Linguagens é assimétrico positivo (cauda à direita).")
else:
    print("O histograma de Linguagens é assimétrico negativo (cauda à esquerda).")

# 7. Histogramas de Redação e Linguagens com range fixo de 0 até 1000
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(df['Redação'], bins=50, range=[0, 1000], edgecolor='black')
plt.title('Histograma de Redação (Range 0-1000)')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
plt.hist(df['Linguagens'], bins=50, range=[0, 1000], edgecolor='black')
plt.title('Histograma de Linguagens (Range 0-1000)')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()  # Exibir o gráfico diretamente

# 8. Boxplot de todas as disciplinas
plt.figure(figsize=(10, 6))
plt.boxplot([df['Redação'], df['Matemática'], df['Linguagens'], df['Ciências humanas'], df['Ciências da Natureza']],
            labels=['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da Natureza'])
plt.title('Boxplot das Disciplinas')
plt.ylabel('Nota')
plt.show()  # Exibir o gráfico diretamente

# 9. Remover outliers e verificar impacto na média nacional
def remover_outliers(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    return df[(df[coluna] >= lim_inf) & (df[coluna] <= lim_sup)]

df_sem_outliers = remover_outliers(df, 'Nota_Ponderada')
media_sem_outliers = df_sem_outliers['Nota_Ponderada'].mean()
desvio_padrao_sem_outliers = df_sem_outliers['Nota_Ponderada'].std()

impacto_media = ((media_ponderada - media_sem_outliers) / media_ponderada) * 100
print(f"\nMédia sem outliers: {media_sem_outliers:.2f}")
print(f"Desvio padrão sem outliers: {desvio_padrao_sem_outliers:.2f}")
print(f"Impacto na média nacional: {impacto_media:.2f}%")

# 10. Melhor medida de tendência para substituir valores nulos
df_moda = df.fillna(df.mode().iloc[0])
df_media = df.fillna(df.mean())
df_mediana = df.fillna(df.median())

media_original = df.mean()
media_moda = df_moda.mean()
media_media = df_media.mean()
media_mediana = df_med
