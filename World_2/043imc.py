peso = float(input('Digite seu peso (kg):'))
altura = float(input('Digite sua altura (em metros):'))
imc = peso / (altura**2)
print('Seu Índice de Massa Corporal (IMC) é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL.')
elif 18.5 < imc <= 25:
    print('Parabéns! Você está no peso ideal.')
elif 25 < imc <= 30:
    print('Você está na categoria de SOBREPESO')
elif 30 < imc <= 40:
    print('Cuidado. Seu índice é de OBESIDADE!')
else:
    print('Muito cuidado! Seu índice é de OBESIDADE MÓRBIDA!')
