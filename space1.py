#!/usr/bin/env python2
import random
import os

def start():

    os.system("clear")
    print "starship takeoff"

    g = random.randint(1,2)
    w = random.randint(1,2)
    r = g * w
    tries = 3

    print "gravity ", g

    count_tries = 0 
    force = 0

    while count_tries < tries and force != r:
        print "enter force","r is ",r
        force = int(raw_input("input force:"))
        if force < r:
            print "too low"
        elif force > r:
            print "too high"
        elif force == r:
            print "that seems right"
        count_tries +=1

    if r == force:
        print "you is winner!"
    else:
        print "you is looser :("

if __name__ == '__main__':
    start()
