def calculate():
    operation = input('''
Escolha a operação desejada:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Insira o primeiro número: '))
    number_2 = int(input(‘Insira o segundo número:  '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou uma operação válida, por favor execute o comando novamente')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Você quer calcular de novo?
Digite S para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print(‘Até mais!')
    else:
        again()

calculate()
