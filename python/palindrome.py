num=int(input("Enter a num"))
reverse=0
a=num     //temp var
while(num>0): //num=0 so this condition
  digit=num%10
  reverse=reverse*10+digit
  num=num//10
if(a==reverse):
  print("Its palindrome")
else:
  print("Not palindrome")