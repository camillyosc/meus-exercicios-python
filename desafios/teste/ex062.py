pt = int(input('Digite o primeiro termo da sua progressão aritmética:'))
r = int(input('Digite qual será a razão dela:'))
c = 0
while c < 10:
  termo = pt + (c) * r
  print(termo)
  c += 1 
print('Essa é a PA do seu número!')
maistermos = int(input('Você quer mostrar mais termos? Quantos?'))
while maistermos != 0:  
  novocontador = 0
  while novocontador < maistermos:
    termo = pt + (c) * r
    print(termo)
    c += 1 
    novocontador += 1
  maistermos = int(input('Você quer mostrar mais termos? Quantos? '))
  if maistermos == 0:
    print('Seu programa foi finalizado!')
  
 
 


  
  
