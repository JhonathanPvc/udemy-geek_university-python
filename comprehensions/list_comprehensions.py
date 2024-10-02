"""
  List Comprehensions
"""

# Exemplo 1

numeros: list[int] = [1, 2, 3, 4, 5]

resultado = [numero*2 for numero in numeros]
print(f'Resultado: {resultado}')

# Exemplo 2
lista_numeros = [2, 3, 5, 7, 9, 11, 44, 6, 77, 9, 0]
numeros_pares = [numero for numero in lista_numeros if numero % 2 == 0]
numeros_impares = [numero for numero in lista_numeros if numero % 2 != 0]

print(f'Numeros pares: {numeros_pares}')
print(f'Numeros impares: {numeros_impares}')
