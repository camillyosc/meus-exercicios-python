da = int(input('Por quantos dias o carro foi alugado?'))
kr = float(input('Quantos KM foram rodados?'))
t = (60*da) + (kr*0.15)
print(f'O total a pagar vai ser R${t:.2f}!')