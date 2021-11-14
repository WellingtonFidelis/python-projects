# -*- coding: utf-8 -*-
# Calculadora em Python

from string import Template
from os import system


class Calculator():
    def __init__(self):
        pass

    def add(digit1, digit2):
        result = digit1 + digit2
        return (result)

    def subtract(digit1, digit2):
        result = digit1 - digit2
        return (result)

    def multiply(digit1, digit2):
        return (digit1 * digit2)

    def divide(digit1, digit2):
        return (digit2 / digit2)


screen = Template("""
''''''''''''''''''''''''''''''
$n1 $op $n2
''''''''''''''''''''''''''''''
Digite:
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
''''''''''''''''''''''''''''''
$commands
""")

system('clear')

while True:
    option_user = input(screen.substitute(
        n1='', op='', n2='', commands='Escolha uma opção.'
    ))
    print(option_user)
    print(type(option_user))

    if option_user in (1, 2, 3, 4):
        num1 = float(input(screen.substitute(
            n1='', op='', n2='', commands='Digito o 1º número:'
        )))
        system('clear')
        print(screen.substitute(
            n1=num1, op='', n2='', commands=''
            ))
        system('clear')
        num2 = float(input(screen.substitute(
            n1=num1, op='', n2='', commands='Digito o 2º número:'
        )))

        if option_user == '1':
            print(num1, "+", num2, "=", Calculator.add(num1, num2))

        elif option_user == '2':
            print(num1, "-", num2, "=", Calculator.subtract(num1, num2))

        elif option_user == '3':
            print(num1, "*", num2, "=", Calculator.multiply(num1, num2))

        elif option_user == '4':
            print(num1, "/", num2, "=", Calculator.divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        calculate_again = input("Deseja fazer um novo cálculo (Sim[s] / Não[n]): ")
        if calculate_again == "n":
            break

    else:
        print("Invalid Input")
#
#print("\nSelecione o número da operação desejada: \n")
#print("1 - Soma")
#print("2 - Subtração")
#print("3 - Multiplicação")
#print("4 - Divisão")

#escolha = input("\nDigite sua opção (1/2/3/4): ")
#
#num1 = int(input("\nDigite o primeiro número: "))
#num2 = int(input("\nDigite o segundo número: "))

#if escolha == '1':
#    print("\n")
#    print(num1, "+", num2, "=", Calculator.add(num1, num2))
#    print("\n")
#
#elif escolha == '2':
#    print("\n")
#    print(num1, "-", num2, "=", subtract(num1, num2))
#    print("\n")
#
#elif escolha == '3':
#    print("\n")
#    print(num1, "*", num2, "=", multiply(num1, num2))
#    print("\n")
#
#elif escolha == '4':
#    print("\n")
#    print(num1, "/", num2, "=", divide(num1, num2))
#    print("\n")
#
#else:
#    print("\nOpção Inválida!")
#
#
#
#print(screen.substitute(n1='3', op='+', n2='4', commands='Example'))
