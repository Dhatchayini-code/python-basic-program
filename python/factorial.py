f=1     //for logic
a=int(input("Enter a number"))
if a<0:  //negative number
   print("factorial cannot be find")
elif a==0:  //0!=1
   print("the factorial of a is 1")
else:
  for i in range(1,a+1):  //a=5,a+1=(6) is excluded
     f=f*1
  print("the factorial of a number is",f)