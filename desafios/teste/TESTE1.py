sexo = str(input('Informe seu sexo [m/f] : ')).lower() [0]
while sexo != 'm' and sexo != 'f' :
  sexo = str(input('Dado inválido. Informe seu sexo novamente! [m/f]: ')).lower() [0]
if sexo == 'm':
  print('Dado registrado com sucesso! Você é do sexo masculino.')
else:
  print('Dado registrado com sucesso! Você é do sexo feminino.')
