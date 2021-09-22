d = int(input('Durante quantos dias você utilizou o veículo? '))
km = float(input('Quantos quilômetros percorreu? '))
p = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(p))
