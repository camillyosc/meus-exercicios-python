cont = 0
soma = 0
continuar = "S"
numero_lista = []
while continuar != "N":
    numero = int(input("Digite um número:"))
    continuar = input("Quer continuar S/N:").upper()
    cont += 1
    soma += numero
    numero_lista.append(numero)
    

maior = max(numero_lista)
menor = min(numero_lista)
media = soma / cont

print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')





 
