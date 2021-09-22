casa = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Qual o seu salário atual? R$ '))
anos = int(input('Em quantos anos você pretende pagar esse empréstimo?'))
prestacao = casa/(anos*12)
aprov = sal * 0.3
if prestacao <= aprov:
    print('Parabéns, seu empréstimo foi aprovado.')
    print('O valor das prestações ficará em R${:.2f} mensais'.format(prestacao))
else:
    print('Infelizmente seu empréstimo foi negado.')
