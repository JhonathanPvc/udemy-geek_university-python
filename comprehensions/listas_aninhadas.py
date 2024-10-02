"""
  Listas Aninhadas 

  Em outras linguagens sao os arrays
"""
# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
print(type(listas))

# Acessando os dados
print(listas[0][2])  # 3
print(listas[2][2])  # 9

print('\n')

# Iterando com loop

for lista in listas:
    for numero in lista:
        print(numero)

# Iterando com List Comprehension
print('\n')
[[print(valor) for valor in lista] for lista in listas]
