# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

    +---+
    |   |
    |
    |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |   |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|\
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|\
    |  /
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|\
    |  / \
    |
=========''']


# Classe
class Hangman:
    # Método Construtor
    def __init__(self, word):
        pass

    # Método para adivinhar a letra
    def guess(self, letter):
        pass

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        pass

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        pass

    # Método para não mostrar a letra no board
    def hide_word(self):
        pass

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        pass


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    path = '/home/tom/Documents/Projects/python-projects/python-fundamentals-data-analysis-3.0/PythonFundamentos/Cap05/Lab03'
    with open(path + "/palavras.txt", "rt") as f:
        bank = f.readlines()
        print(bank)
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    print(game)
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra
    # e faz a leitura do caracter

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
