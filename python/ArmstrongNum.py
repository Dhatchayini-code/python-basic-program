num=int(input("Enter a number"))
sum=0
order=len(str(num))//to find len for power
a=num //temp variable
while(num>0):
    digit=num%10
    sum+=digit**order
    num=num//10
if(sum==a): //sum=153,num=0 so "a"=="num" it have 153
    print("Armstrong number")
else:
    print("not an Armstrong Number")