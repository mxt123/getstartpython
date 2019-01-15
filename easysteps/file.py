poem = 'blah blah blah\n'
poem += '2lah\n'
poem += '3lah\n'

file = open('poem.txt','w')
file.write(poem)
file.close()

file = open('poem.txt','a')
file.write('xxxxxxxxxxxx')
file.close()

file = open('poem.txt','r')

for line in file:
    print(line, end='')
print('\n')
file.close()
