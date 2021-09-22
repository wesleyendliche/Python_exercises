n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
so = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#print('A soma é {}, a subtração é {}, o produto é {}'.format(so, su, m))
print('A \033[4;30msoma\033[m é {}, a \033[4;31msubtração\033[m é {}, \n O \033[4;32mproduto\033[m é {},'.format(so, su, m), end=' ')
print('A \033[4;33mdivisão\033[m é {:.2f}, \n A \033[4;34mdivisão inteira\033[m é {}, \n E a \033[4;35mpotência\033[m {}'.format(d, di, e))
