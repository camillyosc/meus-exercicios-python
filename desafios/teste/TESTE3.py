pvalor = int(input('Digite o primeiro valor:'))
svalor = int(input('Digite o segundo valor:'))
valores = []
valores.append(pvalor)
valores.append(svalor)



print ('''
       Somar [1] 
       Multiplicar [2]
       Maior [3]
       Novos números [4]
       Sair do programa [5]''')

while True:

 opcao = int(input('Qual é sua opção:'))


 if opcao == 1:
  soma = pvalor + svalor
  print(soma)
 elif opcao == 2:
  multiplica = pvalor * svalor
  print(multiplica)
 elif opcao == 3:
  maior = max(valores)
  print(maior)
 elif opcao == 4:
  pvalor = int(input('Digite novo primeiro valor:'))
  svalor = int(input('Digite novo segundo valor:'))
 else:
  print('Programa encerrado!')
  break