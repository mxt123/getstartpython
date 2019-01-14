basket = ['Apple', ' Bun', 'Cola' ]
crate = ['Egg', 'Fig', 'Grape']

print(basket)
print('size:',len(basket))
basket.append('damson')
print('appended',basket)
print('last item removed:',basket.pop())
print(basket)

basket.extend(crate)
print('extended', basket)
del basket[1]
print('removed',basket)
del basket[1:3]
print('Slice removed:',basket)
