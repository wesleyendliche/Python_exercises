from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
sexo = str(input('Você é HOMEM ou MULHER? Digite H ou M. ')).upper()
idade = date.today().year - ano
if idade == 18 and sexo == 'h':
    print('Você está com 18 anos. Deve se alistar IMEDIATAMENTE!')
elif idade < 18 and sexo == 'h':
    print('Você está com {} e deve se alistar daqui a {} anos'.format(idade, 18-idade))
elif sexo == 'M':
    print('No Brasil, mulheres não precisam se alistar.')
else:
    print('Você está com {} anos. Já deveria ter se alistado há {} anos!'.format(idade, idade-18))
