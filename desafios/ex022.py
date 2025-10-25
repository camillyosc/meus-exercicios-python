'''nc = input('Digite seu nome completo:')
nc = nc.upper()
nm = nc.lower()
ql = len(list(filter(str.isalpha, nc)))
pn = nc.split()[0]
cpn = len(list(filter(str.isalpha, pn))) 
print(f'{nc}, {nm}, a quantidade de letras são {ql} e a quantidade de letras do primeiro nome é {cpn}')'''

#existe essa maneira
nome = str(input('Digite seu nome completo:')).strip()
print(f'Seu nome em letras maiúsculas é : {nome.upper()}')
print(f'Seu nome em letras minúsculas é : {nome.lower()}')
print(f'A quantidade de letras é: {len(nome) - nome.count(' ')}')
print(f'A quantidade de letras do primeiro nome é {nome.find(' ')}')


