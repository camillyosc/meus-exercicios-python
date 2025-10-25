'''salario = float(input('Qual é o seu salário?:'))
if salario > 1250:
  aumentoum = salario * 0.1
  valorfinalum = salario + aumentoum
  print(f'O valor final de seu salário é maior: {valorfinalum}')
else:
  aumentodois = salario * 0.15
  valorfinaldois = salario + aumentodois
  print(f'O valor final de seu salário é menor: {valorfinaldois}')'''


#DA PRA FAZER ASSIM TBM:
salario = float(input('Qual é o seu salário?:'))
if salario <= 1250:
  novo = salario + (salario * 15 / 100)
else: 
  novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar {novo:.2f}')