frase = str(input('Escreva uma frase e descubra se ela é um palíndromo ou não:'))
fraselimpa = frase.strip()
frasein = frase[::-1].strip()
if frase == frasein:
  print('Sua frase é um palíndromo!')
else:
  print('Sua frase NÃO é um palíndromo!')
