s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 #simplificando cont = cont + 1
        s += c  #simplificando s = s + 1
print('A soma de todos os {} números solicitados é de {}.'.format(cont, s))
