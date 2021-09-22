sal = float(input('Digite seu salário atual: R$'))
aum1 = sal * 0.10 + sal
aum2 = sal * 0.15 + sal
if sal > 1250.00:
    print('Com o reajuste, seu salário de R${:.2f} passará a ser R${:.2f}'.format(sal, aum1))
else:
    print('Com o reajuste, seu salário de R${:.2f} passará a ser R${:.2f}'.format(sal, aum2))
