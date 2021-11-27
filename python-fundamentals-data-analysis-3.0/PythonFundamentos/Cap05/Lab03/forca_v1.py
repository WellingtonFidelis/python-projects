# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from os import system

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<
                          |
    +---+                 |
    |   |                 |
    |                     |
    |                     |
    |                     |
    |                     |
===========================''', '''

>>>>>>>>>>Hangman<<<<<<<<<<
                          |
    +---+                 |
    |   |                 |
    |   O                 |
    |                     |
    |                     |
    |                     |
===========================''', '''

>>>>>>>>>>Hangman<<<<<<<<<<
                          |
    +---+                 |
    |   |                 |
    |   O                 |
    |   |                 |
    |                     |
    |                     |
===========================''', '''

>>>>>>>>>>Hangman<<<<<<<<<<
                          |
    +---+                 |
    |   |                 |
    |   O                 |
    |  /|                 |
    |                     |
    |                     |
===========================''', '''

>>>>>>>>>>Hangman<<<<<<<<<<
                          |
    +---+                 |
    |   |                 |
    |   O                 |
    |  /|\\               |
    |                     |
    |                     |
===========================''', '''

>>>>>>>>>>Hangman<<<<<<<<<<
                          |
    +---+                 |
    |   |                 |
    |   O                 |
    |  /|\\               |
    |  /                  |
    |                     |
===========================''', '''

>>>>>>>>>>Hangman<<<<<<<<<<
                          |
    +---+                 |
    |   |                 |
    |   O                 |
    |  /|\\               |
    |  / \\               |
    |                     |
===========================''']


# Classe
class Hangman:
    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        result = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                result += '_'
            else:
                result += letter
        return result

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ', [letter for letter in self.missed_letters])
        print()
        print('\nLetras corretas: ', [letter for letter in self.guessed_letters])
        print()


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    file_words = './Lab03/palavras.txt'
    with open(file=file_words, mode='rt', encoding='utf-8') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank) - 1)].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    print(game.word)
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra
    # e faz a leitura do caracter
    while not game.hangman_over():
        system('clear')
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    system('clear')
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        # print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
