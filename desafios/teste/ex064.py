quantosn = 0
soma = 0
n = int(input('Digite um númerooo:'))
while n != 999:
    quantosn += 1
    soma += n
    n = int(input('Digite um número:'))
print(f'O total de números digitados foi {quantosn} e a soma entre eles é de {soma}')
if n == 999:
    print('Seu programa encerrou!')
