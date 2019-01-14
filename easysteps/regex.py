from re import *

pattern = \
compile('[^@]+@[^@]+\.[^@]+')

cont = True

while cont  :
    address = input('Enter email:') 
    if address == 'exit' : 
        break
    else :
        if pattern.match(address):
            print('valid')
        else:
            print('invalid')
