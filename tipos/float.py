"""
Tipos Float ou Real, Decimal
"""

#ERRADO
valor = 1,66
print(valor)
print(type(valor))

#CERTO
valor = 1.66
print(valor)
print(type(valor))

#DUPLA ATRIBUICAO
valor1, valor2 = 1, 33
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#CONVERSAO
resultado = int(valor)
print(resultado)
print(type(resultado))