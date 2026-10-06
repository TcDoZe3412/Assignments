c = 0
l = []
mx = 0 
mn = 0

while c < 10:
    t = int(input("enter the  number: "))
    l.append(t)
   
    if len(l) == 1: 
        mx = l[0]
        mn = l[0]
    else:
        if l[c] > mx: 
            mx = l[c]
        if l[c] < mn: 
            mn = l[c]
            
    c += 1

print(f"the max is {mx} and the min is {mn}")
