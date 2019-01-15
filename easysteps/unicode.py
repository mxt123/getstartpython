<<<<<<< HEAD
s = ''
print(s)
=======
import unicodedata

s = ('répertoire')
print(s)
print('Type:', type(s), '\tlength:', len(s))

for i in range(len(s)) :
    print(s[i], unicodedata.name(s[i]), sep=':')

s = s.encode('utf-8')
print('\nDecoded String:',s)
print('Type:', type(s), '\tLength:', len(s))

>>>>>>> wip
