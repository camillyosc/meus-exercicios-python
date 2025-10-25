pesos = []
for c in range(0,5):
  peso = float(input('Digite seu peso:'))
  pesos.append(peso)
maior_numero = max(pesos)
menor_numero = min(pesos)
print(f'O menor peso foi {menor_numero}, e o maior foi {maior_numero}.')
 