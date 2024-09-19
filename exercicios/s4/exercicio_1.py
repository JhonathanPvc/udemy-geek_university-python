"""
  Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""
def retorna_numero_maior(numero1, numero2):
  numeroMaior: int = 0
  numeroMenor: int = 0
  
  if numero1 > numero2:
    numeroMaior = numero1
    numeroMenor = numero2  
  elif numero1 == numero2:
    return print('Os numeros são IGUAIS!')
  else :
    numeroMaior = numero2
    numeroMenor = numero1

  return print(f'O numero {numeroMaior} é maior que {numeroMenor}')

print('\nOla! Digite 2 numeros e eu vou dizer qual é o maior')
print('Digite o primeiro numero:')
numero1: int = int(input())
print('Digite o segundo numero:')
numero2: int = int(input())

retorna_numero_maior(numero1, numero2)