from Bird import *

chick = Bird('Cheep, Cheep!')
chick.age = '1 week'

print('\nChick says:',chick.talk())
print('Chick age:',chick.age)
chick.age = '2 weeks'
print('Chick age:',chick.age)
setattr(chick,'age','3 weeks')
print('\nChick Attributes...')

for attrib in dir(chick):
    if attrib[0] != '_':
        print(attrib,':',getattr(chick,attrib))

delattr(chick, 'age')

print('\nChick age attribute?', hasattr(chick,'age'))
