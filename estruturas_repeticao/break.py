"""
Saindo de loops com break

# Exemplo 1
for numero in range(1,11):
  if (numero == 8):
    break
  else:
    print(numero)
print('Saiu do LOOP!')

"""
# Exemplo 2
while True:
  comando = input("Digite 'Sair' para parar! \n")
  if comando == 'Sair':
    break