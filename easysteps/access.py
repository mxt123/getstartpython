file = open('example.txt','w')
print('File name', file.name)
print('File Open Mode:', file.mode)
print('Readable:', file.readable())
print('Writeable:', file.writable())

def get_status(f) :
    if (f.closed != False) :
        return 'closed'
    else:
        return 'open'

print('File status', get_status(file))
file.close()
print('File status', get_status(file))
