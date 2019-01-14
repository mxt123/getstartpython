chars = ['A','B','C']
fruit = {'Apple','Banana','Cherry'}
dict = {'name':'mike','ref':'Python'}

for item in chars :
    print(item)

for item in zip (chars, fruit) :
    print(item, end = '')

print("\n")

for key,value in dict.items() :
    print(key,'=',value)

for key in dict.keys() :
    print(dict[key])
