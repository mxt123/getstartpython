for i in range(1,4) :
   for j in range (1,4) :
        if i == 1 and j == 1 :
            print('continue inner loop at i=1 j=1')
            continue
        elif i == 2 and j == 1 :
            print('break inner loop at i=2 and j=1')
            break
        print('i:j',i,':',j)
