num = int(input('Qual número inteiro você desejaria converter? '))
print('''Digite \033[1;33m[1]\033[m para convertê-lo em número binário
\033[1;33m[2]\033[m para octal, 
Ou \033[1;33m[3]\033[m para hexadecimal:''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
