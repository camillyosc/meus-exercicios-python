import datetime
ano = int(input('Digite seu ano de nascimento:'))
idade = (datetime.date.today().year - ano)
if idade <= 9:
  print('Você é da categoria mirim.')
elif idade > 9 and idade <=14:
  print('Você é da categoria infantil.')
elif idade > 14 and idade <=19:
  print('Você é da categoria junior.')
elif idade > 19 and idade <=25:
  print('Você é da categoria sênior.')
else:
  print('Você é da categoria master.')