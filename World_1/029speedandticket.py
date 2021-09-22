vel = float(input('Você está rodando a quantos km/h? '))
if vel <= 80:
    print('Muito bem! Continue com segurança.')
else:
    print('Você excedeu o limite de 80km/h e foi multado. A multa é de R${:.2f}.'.format((vel-80)*7))
