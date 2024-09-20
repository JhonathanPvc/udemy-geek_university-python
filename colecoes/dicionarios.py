"""
  Dicionarios: Sao colecoes do tipo CHAVE/VALOR
"""

paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'py': 'Paraguai'
}
print(f'Valor dicionario paises: {paises}')
print(f'Tipo dicionario paises: {type(paises)}')

# Acessando os elementos

# Forma 1
print(paises['br'])

# Forma 2 (get)
print(paises.get('ch'))  # Nao da erro ao tentar ler uma chave invalida

# ----------------------------------------------------------------

localidades = {
    (35.558, 39.464): 'Escritorio em Tokio',
    (22.428, 29.448): 'Escritorio em Londres',
    (41.218, 49.355): 'Escritorio em Sao Paulo',
}
print(f'Localidades: {localidades}')
print(type(localidades))

# ----------------------------------------------------------------

# Adicionar elementos

receita = {
    'Janeiro': 100,
    'Fevereiro': 355,
    'Marco': 820,
}
print(f'Receitas: {receita}')
print(type(receita))

# Forma 1
receita['Abril'] = 789
print(f'Receitas: {receita}')

# Forma 2
receita.update({'Maio': 128})
print(f'Receitas: {receita}')
