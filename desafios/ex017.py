'''from math import pow, sqrt
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
s = pow(co,2) + pow(ca,2)
h = sqrt(s)
print(f'A hipotenusa do seu triângulo é {h:.2f}')'''

#Da pra fazer dessa maneira:
from math import hypot
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print(f'A hipotenusa do seu triângulo é {hi:.2f}')