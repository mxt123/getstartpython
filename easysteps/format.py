snack = '{} and {}'.format('Burger', 'Fries')
print('\nReplaced:', snack)

snack = '{1} and {0}'.format('Burger', 'Fries')
print('\nReplaced:', snack)

snack = '%s and %s' % ('Burger', 'Fries')
print('\nReplaced:', snack)

message = '%d %s %4.2f' % (1, 'thing', 2.32) 
print('\nReplaced:', message)
