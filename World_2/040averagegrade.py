n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1+n2)/2
if média >= 7.0:
    print('Parabéns, sua média foi {:.1f} e você está {}APROVADO{}.'.format(média, '\033[1;32m', '\033[m'))
elif 7.0 > média >= 5.0: #ou 5.0 <= média < 7.0
    print('Sua média foi de {:.1f}. Você está de {}RECUPERAÇÃO{}.'.format(média, '\033[1;33m', '\033[m'))
elif média < 5.0:
    print('Sua média foi de {:.1f}. Infelizmente, você está {}REPROVADO{}.'.format(média, '\033[1;31m', '\033[m'))
