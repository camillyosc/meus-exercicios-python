'''nc = str(input('Digite o nome da sua cidade:'))
nomec = nc.split()
cs = nomec[0].lower()   
print("santo" in cs)'''


#outra maneira de fazer:
nomecidade = str(input('Digite o nome da sua cidade')).strip()
print(nomecidade[:5].upper() == 'SANTO')