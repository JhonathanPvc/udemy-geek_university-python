"""
  Utilizamos loop para iterar sobre a sequencias ou sobre valores iteraveis

nome = "Jhonathan Cordeiro"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Iterando String
for letra in nome:
  print(letra)

print('\n')
# Iterando Numeros
for numero in lista:
  print(numero)
  
print('\n')
# Iterando Range
for numero in numeros:
  print(numero)
"""
quantidade_for = int(input('Quantas vezes o FOR vai rodar ? '))

for n in range(1, (quantidade_for+1)):
  print(f'Imprime {n}')