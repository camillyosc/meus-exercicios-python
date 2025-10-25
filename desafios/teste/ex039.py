import datetime
ano = int(input('Digite o ano de seu nascimento:'))
idade = (datetime.date.today().year - ano)
anosfalta = 18 - idade
anospassou = idade - 18
if idade == 18:
  print('Já é hora de se alistar!')
elif idade < 18:
  print(f'Ainda não é hora! Falta {anosfalta} anos!')
elif idade > 18:
  print(f'Já passou da hora de se alistar! {anospassou} anos!')
