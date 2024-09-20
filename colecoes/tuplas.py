"""
  Tuplas. Sao representadas por ()
  Porque utilizar tuplas ? 
    - Sao mais rapidas que listas
    - Deixam o codigo mais seguro (Tuplas sao imutaveis)
"""
tupla1: tuple = (1, 2, 3, 4, 5, 6)
print(F'Valor Tupla1: {tupla1}')
print(f'Tipo da Tupla1: {type(tupla1)}\n')

tupla2 = 1, 2, 3, 4, 5, 6
print(F'Valor Tupla2: {tupla2}')
print(f'Tipo da Tupla2: {type(tupla2)}\n')

tupla3 = (5)  # ISSO NAO E UMA TUPLA
print(F'Valor Tupla3: {tupla3}')
print(f'Tipo da Tupla3: {type(tupla3)}\n')

tupla4 = (5, )  # ISSO E UMA TUPLA
print(F'Valor Tupla4: {tupla4}')
print(f'Tipo da Tupla4: {type(tupla4)}\n')

tupla5 = tuple(range(11))
print(F'Valor Tupla5: {tupla5}')
print(f'Tipo da Tupla4: {type(tupla5)}\n')
