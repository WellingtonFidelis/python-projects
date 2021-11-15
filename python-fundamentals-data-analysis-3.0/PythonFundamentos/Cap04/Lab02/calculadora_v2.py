# -*- coding: utf-8 -*-
# Calculator with Python
# at 2021-11
# By Wellington Fidelis

# To do
#
# -[x] Create screen using Template
# -[x] Create repeating structure
# -[x] Create rules to call operations
# -[x] Create class Calculator
# -[x] Update rules to call operations adding class method of Calculator
# -[x] Commit code

# Imports
from string import Template
from os import system


class Calculator():
    def add(self, digit1, digit2):
        result = digit1 + digit2
        return result

    def subtract(self, digit1, digit2):
        result = digit1 - digit2
        return result

    def multiply(self, digit1, digit2):
        result = digit1 * digit2
        return result

    def divide(self, digit1, digit2):
        result = digit1 / digit2
        return result

    def getOperator(self, option):
        operators = {
                1: '+',
                2: '-',
                3: '*',
                4: '/'
                }
        return operators.get(option)


screen = Template("""
        ''''''''''''''''''''''''''
        $n1 $op $n2 = $result
        ''''''''''''''''''''''''''
        Digite:
            [1] Soma
            [2] Subtração
            [3] Multiplicação
            [4] Divisão
        ''''''''''''''''''''''''''
        $commands
        """)

while True:

    system('clear')

    option_user = input(screen.substitute(
        n1='',
        op='',
        n2='',
        commands='Escolha uma opção.',
        result=''
        ))

    if option_user in (1, 2, 3, 4):

        result = 0
        operator = Calculator().getOperator(option_user)

        system('clear')

        num1 = float(input(screen.substitute(
            n1='',
            op=operator,
            n2='',
            commands='Digite o 1º número:',
            result=''
            )))

        system('clear')

        print(screen.substitute(
            n1=num1,
            op=operator,
            n2='',
            commands='',
            result=''
            ))

        system('clear')

        num2 = float(input(screen.substitute(
            n1=num1,
            op=operator,
            n2='',
            commands='Digite o 2º número:',
            result=''
            )))

        system('clear')

        print(screen.substitute(
            n1=num1,
            op=operator,
            n2=num2,
            commands='',
            result=''
            ))

        if option_user == 1:
            result = Calculator().add(num1, num2)

        elif option_user == 2:
            result = Calculator().subtract(num1, num2)

        elif option_user == 3:
            result = Calculator().multiply(num1, num2)

        elif option_user == 4:
            result = Calculator().divide(num1, num2)

        system('clear')

        print(screen.substitute(
            n1=num1,
            op=operator,
            n2=num2,
            commands='',
            result=result
            ))

        calculate_again = input("Cálcular novamente? Sim[1] / Não[0]: ")

        if int(calculate_again) == 0:
            break

    else:
        print('Opção inválida!')
