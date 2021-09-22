num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('{}{}{} é o maior.'.format('\033[1;36m', num1, '\033[m'))
elif num1 == num2:
    print('Os {}dois valores{} são iguais'.format('\033[4;33m', '\033[m'))
elif num2 > num1:
    print('{}{}{} é o maior.'.format('\033[1;36m', num2, '\033[m'))
