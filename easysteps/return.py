def sum(a,b):
    if a == 5 :
        return a 
    return a + b

#print(sum(8,4))
#print(sum(5,4))

num = input('Enter an integer:')

def square(num):
    if not num.isdigit() :
        return 'invalid'
    num = int(num)
    return num * num

print('num sq:', square(num))
