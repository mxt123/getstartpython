from Bird import *
print('\nClass Instances Of:\n',Bird.__doc__)
polly = Bird('Squak,Squak')
print('\nNumber of birds:',polly.count)
print('Polly says:', polly.talk())
harry = Bird('Tweet, Tweet!')
print('\nNumber of birds:',harry.count)
print('Harry says:',harry.talk())
print('Bird count:',Bird.count)
