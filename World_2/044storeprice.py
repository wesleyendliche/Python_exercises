pn = float(input('Preço total das compras R$'))
um = pn - (pn * 0.1)
dois = pn - (pn * 0.05)
tres = pn / 2
quatro = pn + (pn * 0.2)
print('[ 1 ] Pagamento à vista no dinheiro/cheque')
print('[ 2 ] Pagamento à vista no cartão')
print('[ 3 ] Pagamento em 2x no cartão')
print('[ 4 ] Pagamento em 3x ou mais no cartão')
op = int(input('Digite a forma de pagamento:'))
if op == 1:
    print('Você terá um desconto de 10% e sua compra sairá a R${:.2f}.'.format(um))
elif op == 2:
    print('Sua compra terá desconto de 5% e sairá a R${:.2f}.'.format(dois))
elif op == 3:
    print('Sua compra de R${:.2f} será dividida em duas parcelas de R${:.2f} cada.'.format(pn, tres))
elif op == 4:
    parc = int(input('Digite em quantas vezes quer pagar:'))
    juros = quatro / parc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parc, juros))
    print('Sua compra de R${:.2f} passará a custar R${:.2f}.'.format(pn, quatro))
else:
    print('\033[1;31mOpção inválida. Tente novamente.\033[m')
