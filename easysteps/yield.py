def incrementer():
    i = 1
    while True:
    #while i < 3:
        yield i
        i += 1

inc = incrementer()

print(next(inc))
print(next(inc))
print(next(inc))


def fibonacci_generator():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

print(type(fib))

for j in fib :
    if j > 100 :
        break
    else:
        print('generated:', j, next(fib))
