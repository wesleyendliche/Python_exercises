from math import hypot
co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
print('O comprimento da hipotenusa é de {:.2f}'.format(hypot(co, ca)))
