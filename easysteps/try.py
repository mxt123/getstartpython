title = 'Python'
day = 32

try:
    if day > 31 :
        raise ValueError('brok')
    print(titel)
except (NameError, IndexError, ValueError) as msg :
    print(msg)
finally:
    print('do this anyway')
