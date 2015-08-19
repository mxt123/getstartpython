#!/usr/bin/env python2

import random
import time

rock=1
paper=2
scissors=3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score=0
computer_score=0

def start():
    print "rock, paper, scissors"
    while game():
        pass
    scores()

def game():
    player=move()
    computer=random.randint(1,3)
    result(player,computer)
    return play_again()

def move():
    while True:
        print
        player=raw_input("Rock=1\nPaper=2\nScissors=3\n")
        try:
            player=int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "oops"

def result(player,computer):
    print "computer threw {0}!".format(names[computer])
    global player_score, computer_score
    if player==computer:
        print "tie"
    else:
        if rules[player] == computer:
            print "win"
            player_score += 1
        else:
            print "lose"
            computer_score += 1

def play_again():
    answer = raw_input("again?")
    if answer in ("y","Y"):
        return answer
    else:
        print "bye"

def scores():
    global player_score, computer_score
    print "P:", player_score
    print "C:", computer_score

if __name__ == '__main__':
    start()
