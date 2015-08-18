#!/usr/bin/env python2

sqr1 = lambda x: x*x

int1 = sqr1(10)

print(int1)

int1 = sqr1(6)

print(int1)

def gen_func(x):
    return lambda y: y**x

cube = gen_func(3)

int2 = cube(3)

print(int2)

