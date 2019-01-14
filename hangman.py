#!/usr/bin/env python2

from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
    """
        +-------+
        |
        |
        |
        |
        |
        |
      =============
    """,
    """
        +-------+
        |       |
        |       O
        |
        |
        |
        |
      =============
    """,
    """
        +-------+
        |       |
        |       O
        |       |
        |
        |
        |
      =============
    """,
    """
        +-------+
        |       |
        |       O
        |      -|
        |
        |
        |
      =============
    """,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |
        |
        |
      =============
    """,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |      /
        |
        |
      =============
    """,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |      / \\
        |
        |
      =============
    """,
    ]
    print graphic[hangman]
    return

def start():
    print "hangman"
    while game():
        pass
    scores()

def game():
    dictionary = ["squirrel","cat","frog","dog","penguin","lion"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score
    
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print "already tried ", letter
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print "sorry,", letter, "isn't in this word."
                else:
                    print "yep, in this word"
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print "choose again"

        hangedman(letters_wrong)
        print " ".join(clue)
        print "guesses: ", letters_tried

        if letters_wrong == tries:
            print "game over"
            print word
            computer_score += 1
        if "".join(clue) == word:
            print "win"
            print word
            player_score += 1
            break
    return play_again()

def guess_letter():
    print
    letter = raw_input("guess letter")
    letter.strip()
    letter.lower()
    print
    return letter

def play_again():
    answer = raw_input("again?")
    if answer in ("Y","y"):
        return answer
    else:
        print "bye"

def scores():
    global player_score, computer_score
    print "p", player_score
    print "c", computer_score

if __name__ == '__main__':
    start()
