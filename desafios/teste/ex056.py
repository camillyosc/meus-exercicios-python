nomehomemmaisvelho = ''
idadehomemmaisvelho = 0
somaidades = 0
mulhermenosvinte = 0

for c in range (1,5):
  print(f'----{c}° PESSOA!----')
  nome = str(input('Digite seu nome:'))
  idade = int(input('Digite sua idade:'))
  sexo= str(input('Digite seu sexo (M/F):')).upper()

  somaidades += idade

  if sexo == 'M' and idade > idadehomemmaisvelho:
    idadehomemmaisvelho = idade
    nomehomemmaisvelho = nome

  if sexo == 'F' and idade < 20:
    mulhermenosvinte += 1


mediaidade = somaidades / 4


print(f'A média das idades é de: {mediaidade}')
print(f'O nome do homem mais velho é {nomehomemmaisvelho} e sua idade é {idadehomemmaisvelho}')
print(f'A quantidade de mulheres com menos de 20 anos é de {mulhermenosvinte}')




  





