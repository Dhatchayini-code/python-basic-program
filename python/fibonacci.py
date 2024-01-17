first=0
second=1
print(first)
print(second)
for i in range(2,10):
   next=first+second
   first=second
   second=next
   print(next)
//frst=0       frst=1     frst=1     frst=2
//sec=1        sec=1      sec=2      sec=3
//next=0+1=1   next=1+1=2 next=1+2=3 next=2+3=5......