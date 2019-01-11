a = input( 'Enter a number:' )
b = input( 'Enter another number:' )

sum = a + b
print( '\nData Type sum:', sum, type(sum) )

sum = int(a) + int(b)
print( '\nData Type sum:', sum, type(sum) )

sum = float(a) + float(b)
print( '\nData Type sum:', sum, type(sum) )

sum = float(a) + int(b)
print( '\nData Type sum:', sum, type(sum) )

sum = int(a) + float(b)
print( '\nData Type sum:', sum, type(sum) )
