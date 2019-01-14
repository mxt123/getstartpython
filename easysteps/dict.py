dict = {'name':'a','ref':'python','sys':'linux','list':[1,2,3],'set':{4,5,6}}
print('whole dict:',dict)
print('list from dictionary element 1',dict['list'][1])
print('random element from set',dict['set'].pop())
print('ref',dict['ref'])
print('\nkeys:',dict)
del dict['name']
dict['user'] = 'tom'
print(dict)
