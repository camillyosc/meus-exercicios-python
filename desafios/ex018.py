from math import cos, sin, tan, radians
ângulo = float(input('Digite seu ângulo:'))
cos = cos(radians(ângulo))
print(f'O cosseno desse ângulo é {cos:.2f}')
sen = sin(radians(ângulo))
print(f'O seno desse ângulo é {sen:.2f}')
tan = tan(radians(ângulo))
print(f'A tangente desse ângulo é {tan:.2f}')