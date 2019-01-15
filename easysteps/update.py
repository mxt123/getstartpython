text = 'xx x x x "asfasfs" xx x x'

with open ('update.txt', 'w') as file:
    file.write(text)
    print('\nFile now closed?:',file.closed)

print('\nFile now closed?:',file.closed)

with open ('update.txt', 'r+') as file:
    text = file.read()
    print('\nString', text)
    print('\nPosition in file now:', file.tell())
    position = file.seek(3)
    print('\nPosition in file now:', file.tell())
    file.write('All Lands')
    file.seek(10)
    file.write('yyyyy')
    file.seek(0)
    text = file.read()
    print('\nstring:', text)

