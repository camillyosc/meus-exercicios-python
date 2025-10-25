valor = float(input('Digite o valor do produto:'))
print("""Escolha a condição de pagamento:
1 - À vista em dinheiro/cheque (10% de desconto)
2 - À vista no cartão (5% de desconto)
3 - Em até 2x no cartão (preço normal)
4 - 3x ou mais no cartão (20% de juros)""")
opcao = int(input('Digite a opção desejada:'))
if opcao == 1:
  desconto = valor * 0.10
  valorfinal = valor - desconto
  print(f'A vista em dinheiro ou cheque. O valor final do seu produto é: R$ {valorfinal}')
elif opcao == 2:
  desconto = valor * 0.05
  valorfinal = valor - desconto
  print(f'A vista no cartão. O valor final do seu produto é: R$ {valorfinal}')
elif opcao == 3:
  parcela = valor / 2
  print(f'Em duas vezes no cartão sua parcela será de {parcela}. O valor total do seu produto é: R$ {valor}')
elif opcao == 4:
  juros = valor * 0.2
  valorfinal = valor + juros
  totalparcela = int(input('Quantas parcelas você quer pagar?'))
  parcela = valorfinal / totalparcela
  print(f'Em {totalparcela} vezes no cartão, o valor será de R${parcela:.2f} com juros. O valor total do seu produto é: R${valorfinal}')
else:
  total = 0
  print('OPÇÃO \33[91m INVÁLIDA \033[m DE PAGAMENTO! TENTE NOVAMENTE!')
