numero = int(input('Digite um número inteiro:'))
print('''Escolha uma das opções para conversão:
    [ 1 ] Converter para base BINÁRIA
    [ 2 ] Converter para base OCTAL
    [ 3 ] Converter para base HEXADECIMAL''')
opcao = int(input('Sua opção:'))
if opcao == 1:
  print(f'O número {numero} convertido para binário é igual a {bin(numero) [2:]}')
elif opcao == 2:
  print(f'O número {numero} convertido para octal é igual a {oct(numero)[2:]}')
elif opcao == 3:
  print(f'O número {numero} convertido para hexadecimal é igual a {hex(numero)[2:]}')
else:
  print('Opção inválida. Tente novamente.')