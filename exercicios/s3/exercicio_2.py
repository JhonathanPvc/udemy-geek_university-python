"""
  Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
"""
soma = 0
def soma_valor(valor):
  retorno = soma+valor
  return retorno

print('Ola! \n Vou pedir para vc digitar 3 valores.')
print('\n')
for x in range(3):
  print(f'Digite o valor {x+1}: ')
  numeroDigitado = int(input())
  soma = soma_valor(numeroDigitado)

print(f'A soma dos valores digitados foi de: {soma}')