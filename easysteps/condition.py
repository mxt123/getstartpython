a = 1
b = 2

print('\nVariable a is :', 'One' if ( a == 1) else 'not one')
print('Variable a is :', 'Even' if ( a % 2 == 0) else 'odd')
print('\nVariable b is :', 'One' if ( b == 1) else 'not one')
print('Variable b is :', 'Even' if ( b % 2 == 0) else 'odd')

max = a if ( a > b ) else b
print (max)
