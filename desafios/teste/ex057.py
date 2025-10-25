sexo = ''
while sexo == 'M' or sexo =='F':
  sexo = str(input('Digite seu sexo: [M/F]')).upper()
  if sexo != 'M' and sexo != 'F':
    incorreto = str (input('Está incorreto! Digite novamente seu sexo: [M/F]')).upper()