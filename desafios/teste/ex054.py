import datetime
idademaior = 0
idademenor = 0
for c in range(0,7):
  anonascimento = int(input('Digite seu ano de nascimento:'))
  idade = datetime.date.today().year - anonascimento
  if idade >= 18:
      idademaior += 1     
  else:
      idademenor += 1

print(f'{idademaior} pessoas são maiores de idade!')
print(f'{idademenor} pessoas são menores de idade!')
      