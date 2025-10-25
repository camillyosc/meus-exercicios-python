pp=float(input('Digite o valor do produto: R$'))
d=0.05*pp
# ou pp*5/100
np=pp-d
# ou novo = preço - (pp*5/100) criar uma só variável
print(f'O valor de seu produto após o desconto é {np:.2f}')