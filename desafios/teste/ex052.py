'''ni = int(input('Digite um número:'))
primo = 0
for c in range(1,ni+1):
  if primo % c == 0:
    primo =+ 1
if primo == 2:
  print('Seu número é primo!')
else:
  ('Seu número não é primo!')'''

'''primo= 0
ni = int(input('Digite um número e descubra se ele é primo ou não:'))
if ni > 1:
  for c in range(1, ni+1):
    if ni % c == 0:
      primo += 1
  if primo == 2: 
    print('Seu número é um número primo!') 
  else: 
    print('Seu número não é primo!') 
else: print('Seu número não é primo!')'''

ni = int(input('Digite um número e descubra se ele é primo ou não:'))

# Inicializa o contador de divisores
contador_divisores = 0

# Verificamos se o número é maior que 1, pois números menores ou iguais a 1 não são primos
if ni > 1:
    for c in range(1, ni + 1):
        if ni % c == 0:
            # Verifica se o divisor é 1 ou ele mesmo
            if c == 1 or c == ni:
                contador_divisores += 1
            else:
                # Se houver outro divisor além de 1 e ele mesmo, já sabemos que não é primo
                contador_divisores = 0
                break
    # Um número primo deve ter exatamente dois divisores: 1 e ele mesmo
    if contador_divisores == 2:
        print('Seu número é um número primo!')
    else:
        print('Seu número não é primo!')
else:
    print('Seu número não é primo!')
