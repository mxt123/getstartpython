zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple:',zoo,'\tLength:', len(zoo))
print(type(zoo))

bag = { 'Red', 'Green', 'Blue' }
bag.add('yellow')
print(bag)
print(bag.pop())
print('yellow' in bag)

box =  { 'Orange', 'Green', 'Blue' }
print(bag.intersection(box))
print(bag.difference(box))
