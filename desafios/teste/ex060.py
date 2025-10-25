n = int(input('Digite um número e descubra seu fatorial:'))
contador = n
fatorial = 1
while contador > 0:  
  fatorial *= contador
  contador -= 1 
print(f'O fatorial de {n}! é {fatorial}')

