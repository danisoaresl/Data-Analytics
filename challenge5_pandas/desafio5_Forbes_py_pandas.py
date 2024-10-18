from pydataset import data

forbes = data('Forbes2000')

print(forbes.head())

empresa_mais_valiosa = forbes.loc[forbes['marketvalue'].idxmax()]
print("\nEmpresa mais valiosa:")
print(empresa_mais_valiosa)

top_10_lucrativas = forbes.nlargest(10, 'profits')
print("\nTop 10 empresas mais lucrativas:")
print(top_10_lucrativas)

media_valores_categoria = forbes.groupby('category')['marketvalue'].mean().nlargest(5)
print("\nMédia de valores das cinco categorias mais valiosas:")
print(media_valores_categoria)
