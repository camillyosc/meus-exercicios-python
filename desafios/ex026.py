frase = input('Digite uma frase:').strip().lower()
qa = frase.count("a")
pv = frase.find("a")+1
uv = frase.rfind("a")+1
print(f'Quantidade de letra "a" {qa}')
print(f'Primeira vez que aparece "a" {pv}')
print(f'Ultima vez que aparece "a" {uv}')