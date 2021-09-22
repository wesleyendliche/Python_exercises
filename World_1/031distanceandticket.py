km = float(input('Qual a distância até o seu destino? '))
p1 = km * 0.5
p2 = km * 0.45
if km <= 200:
    print('Sua passagem custará R${:.2f}'.format(p1))
else:
    print('Sua passagem custará R${:.2f}'.format(p2))
