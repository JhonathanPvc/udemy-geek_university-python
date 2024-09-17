"""
Escopo de variaveis
"""

#Variavel global
numero = 42
print(numero)
print(type(numero))

numero = 'Oi, cara de boi'
print(numero)
print(type(numero))

#Variavel Local
numero = 2

if numero > 10:
    novo_numero = numero+10
    print(novo_numero)

