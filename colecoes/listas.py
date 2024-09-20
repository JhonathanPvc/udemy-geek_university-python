"""
  Listas
"""
lista1: list = [1, 22, 9, 44, 88, 456, 23, 12, 78, 32, 55, 9, 1, 9, 9, 44]
lista2: list = ['J', 'h', 'o', 'n']
lista3: list = []
lista4: list = list(range(11))
lista5: list = list('Jhon')

# Checar valores
numero = 7
if numero in lista4:
    print(f'Encontrei o numero {numero}')
else:
    print(f'Ainda não encontrei o numero {numero}')

# Ordenar lista
lista1.sort()
print(lista1)

# Contar elementos da lista
print(lista1.count(9))

# Adicionar elementos da lista
lista1.append(42)
print(lista1)

lista1.append([44, 55, 652])
print(lista1)

lista1.extend([32, 98, 102, 796, 3])
print(lista1)
