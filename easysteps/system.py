import sys, keyword

print('Python version', sys.version)
print('interpretor', sys.executable)

print('Python module search path')
for dir in sys.path:
    print(dir)

print('keywords')
for word in keyword.kwlist:
    print(word)
