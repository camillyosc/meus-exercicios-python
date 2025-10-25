'''distancia = float(input('Qual a distância da sua viagem em KM?'))
if distancia <= 200:
  menorkm = distancia * 0.50
  print(f'O valor que você vai pagar pela sua passagem é de R${menorkm}')
else:
  maiorkm = distancia * 0.45
  print(f'O valor que você vai pagar pela sua passagem é de R${maiorkm}')'''


#PODE FAZER ASSIM TAMBÉM:
distancia = float(input('Qual a distância  da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {distancia} KM.')
if distancia <= 200:
  preço = distancia * 0.50
else:
  preço = distancia * 0.45
print(f'E o preço que você vai pagar é de {preço:.2f}')




#PODE FAZER ASSIM TBM: (forma simplificada)
'''distancia = float(input('Qual a distância  da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {distancia} KM.')
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de: R${preço:.2f}')'''