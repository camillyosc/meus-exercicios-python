n1 = float(input('Digite sua nota do 1° bimestre:'))
n2 = float(input('Digite sua nota do 2° bimestre:'))
média = (n1+n2) / 2
if média < 5:
  print(f'Você está reprovado! Sua média foi {média}')
elif 7 > média >= 5:
  print(f'Você está de recuperação! Sua média foi {média}')
elif média >= 7:
  print(f'Você está aprovado! Parabéns! Sua média foi {média}')