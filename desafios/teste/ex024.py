'''nome = str(input('Digite seu nome:')).strip()
pn = nome.split()[0].lower()
print('Seu primeiro nome possui silva?')
print('silva' in pn)'''


'''nome = str(input('Digite seu nome:')).strip()
ts = ('silva' in nome[:5].lower())
print(f'Seu primeiro nome possui Silva? {ts}')'''

nome = str(input('Digite seu nome:')).strip()
print(nome[:5].lower() == 'silva')
