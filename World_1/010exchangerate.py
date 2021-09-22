r = float(input('Quanto dinheiro você tem? R$ '))
usd = r / 5.25
cad = r / 4.20
eur = r / 6.19
print('Com R${} você pode comprar U${:.2f}, CAD{:.2f} e €{:.2f}.'.format(r, usd, cad, eur))
