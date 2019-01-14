def echo(user) :
    print('User:', user)

def echo2(user='mr a', lang='abc', sys='123'):
    print('User:',user,'Lang:',lang,'Sys:',sys)

echo('abc')
echo2('abc','123','456')
echo2(lang='a',user='b',sys='c')
echo2()
