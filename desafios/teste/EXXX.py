pesos = []
for c in range(1,6):
  peso = float(input('Digite seu peso:'))
  pesos.append(peso)
peso_max = max(pesos)
peso_min = min(pesos)
print(f'O maior peso foi {peso_max} e o menor foi {peso_min}!')

