a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b:
    if c>a:
     a=c

else:
   if c>b:
     a=c
   else:
     a=b
print(a)
