"""
Created at 10/2021
By Wellington Fidelis
"""
# Calculadora em Python


def calculateResult(operation):
  firstNumber = float(input('Digite o 1º número: '))
  secondNumber = float(input('Digite o 2º número: '))
  if (operation == '+'):
      result = firstNumber + secondNumber
  elif (operation == '-'):
      result = firstNumber - secondNumber
  elif (operation == '/'):
      result = firstNumber / secondNumber
  elif (operation == '*'):
      result = firstNumber * secondNumber

  print('\n{} + {} = {}'.format(firstNumber, secondNumber, result))


userOption = -1

while (int(userOption) != 0):
    print("\n*** Python Calculator ***\n")
    print('---------- Menu ----------')
    print('Somar ---------------- [1]')
    print('Subtrair ------------- [2]')
    print('Dividir -------------- [3]')
    print('Multiplicação -------- [4]')
    print('Sair ----------------- [0]')

    userOption = input('\nEscolha uma opção: ')

    if (int(userOption) > 4):
      print('\nInsira um valor permitido.')
    elif (int(userOption) == 1):
      calculateResult('+')
    elif (int(userOption) == 2):
      calculateResult('-')
    elif (int(userOption) == 3):
      calculateResult('/')
    elif (int(userOption) == 4):
      calculateResult('*')
