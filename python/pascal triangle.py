rows=5
for i in range(rows):
    print(' '*(rows-i),end=" ")
    print(' '.join(map(str,str(11**i))))
