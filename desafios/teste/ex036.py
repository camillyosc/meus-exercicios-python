valorcasa = float(input('Qual o valor da casa que você quer comprar?'))
valorsalario = float(input('Qual o valor do seu salário?'))
quantosanos = int(input('Em quantos anos você quer pagar?'))
meses = quantosanos * 12
prestacao = (valorcasa / meses )
porcentagem = 0.3 * valorsalario
if prestacao <= porcentagem:
  print(f'Você pode financiar sua casa por {prestacao:.3f} reais por mês ')
else:
  print(f'Infelizmente você não pode financiar sua casa!')