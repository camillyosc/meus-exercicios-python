print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Digite a reta a:'))
r2 = float(input('Digite a reta b:'))
r3 = float(input('Digite a reta c:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Você pode formar um triângulo!')
else:
  print('Você não pode formar um triângulo!')