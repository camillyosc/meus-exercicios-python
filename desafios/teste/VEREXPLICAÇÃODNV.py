'''frase = str(input('Digite uma frase e veja se é um palindromo:'))
frasesemespaco = frase.replace(" ","")
fraseinvertida = frasesemespaco[::-1]
if frasesemespaco == fraseinvertida:
  print(f'Sua frase é um palíndromo! {frasesemespaco} é igual a {fraseinvertida} de trás pra frente!')
else:
  print(f'Sua frase não é um palíndromo {frasesemespaco} é igual a {fraseinvertida} de trás pra frente!')'''


frase = str(input('Digite uma frase e veja se é um palindromo:')).strip().upper()
fraseseparada = frase.split()
frasejunta = ''.join(fraseseparada)
inverso = ''
for letra in range(len(frasejunta) - 1 , - 1, - 1):
  inverso += frasejunta[letra]
print(inverso)
