#!/usr/bin/env python2
import random
import os

def start():

    os.system("clear")
    print "starship takeoff"

    gravity = random.randint(1,2)
    weight = random.randint(1,2)
    required_force = gravity * weight
    tries = 3

    print "gravity ", gravity

    count_tries = 0 
    force = 0

    while count_tries < tries and force != required_force :
        print "enter force"
        force = int(raw_input("input force:"))
        if force < required_force:
            print "too low"
        elif force > required_force:
            print "too high"
        elif force == required_force:
            print "that seems right"
        count_tries +=1

    if required_force == force:
        print "you is winner!"
    else:
        print "you is looser :("

if __name__ == '__main__':
    start()
