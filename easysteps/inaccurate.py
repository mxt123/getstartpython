from decimal import *

item = Decimal(0.70)
rate = Decimal(1.05)

tax = item * rate
total = item + tax

print('item:\t','%.2f' % item)
print('tax:\t','%.2f' % tax)
print('total:\t','%.2f' % total)

print('item:\t','%.20f' % item)
print('tax:\t','%.20f' % tax)
print('total:\t','%.20f' % total)
