n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
escolha = 0
print(
  ''' ESCOLHA UMA OPÇÃO:
      [1] somar
      [2] multiplicar
      [3] maior
      [4] novos números
      [5] sair do programa'''
)
while escolha != 5:
  escolha = int(input('Digite aqui sua opção:'))

  if escolha == 1:
    soma = n1 + n2
    print(soma)
  if escolha == 2:
    multiplica = n1 * n2
    print(multiplica)
  if escolha == 3:
    if n1 > n2:
      maior = n1
    else:
      maior = n2
      print(maior)
  if escolha == 4:
   print('Digite novos numeros')
   n1 = int(input('Digite um número:'))
   n2 = int(input('Digite mais um número:'))
if escolha == 5:
  print('Você está saindo do programa!')
