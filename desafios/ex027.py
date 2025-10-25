'''nome = str(input("Digite seu nome:")).strip()
nomecompleto = nome.split()
pn = nomecompleto[0]
un = nomecompleto[-1]
print(f'O primeiro nome é: {pn}')
print(f'O último nome é: {un}')'''


#dessa maneira tambem
nome = str(input("Digite seu nome:")).strip()
nomecompleto = nome.split()
pn = nomecompleto[0]
un = nomecompleto[len(nomecompleto)-1]
print(f'O primeiro nome é: {pn}')
print(f'O último nome é: {un}')