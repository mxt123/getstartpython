#!/usr/bin/env python2
import random
import math
import os

max_tries = 3
angle_tolerance = 10
speed_tolerance = 10000

def start():
    while game():
        pass

def game():
    global max_tries,angle_tolerance,speed_tolerance
    os.system("clear")

    tries = 0

    match = False
    print "INTERGALACTIC GAMES" 
    h = random.randint(1,100) 
    print "you must launch a satellite"
    print "to a height of", h
    print "angle should be ", correct_angle(h)
    print "speed should be ", correct_speed(h)

    while not match and tries < max_tries:
        a_v = get_values()

        a_v_results = calculate(a_v,h)

        match = close_enough(a_v_results)
        tries += 1

        if a_v_results[0] <-angle_tolerance:
            print "too shallow"
        if a_v_results[0] >angle_tolerance:
            print "too steep"
        if a_v_results[1]<-speed_tolerance:
            print "too slow"
        if a_v_results[1]>speed_tolerance:
            print "too fast"

    if match:
        print "you is winner!"
    else:
        print "you is loser!"

    again = raw_input("again? ")
    if again in ("y","Y"):
        return again
    else:
        print "bye bye"

def get_values():
    angle = int(raw_input("angle(0-90)"))
    speed = int(raw_input("speed(0-40000)"))
    return (angle,speed)

def calculate(a_v,h):
    a = a_v[0]
    v = a_v[1]
    a = a - correct_angle(h)
    v = v - correct_speed(h)
    return(a,v)

def correct_speed(h):
    return 3000*math.sqrt(h+1/h)

def correct_angle(h):
    return  math.atan(h/3) *180/math.pi

def close_enough(a_v):
    global angle_tolerance,speed_tolerance
    if abs(int(a_v[0])) < angle_tolerance and abs(int(a_v[1])) < speed_tolerance:
        return True

if __name__ == '__main__':                                        
    start()
