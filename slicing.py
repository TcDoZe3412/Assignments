s = input("enter the string ")
vowels = ['a', 'e', 'i', 'o', 'u']
c = 0
for cha in s:
    for v in vowels:
        if v == cha:
            c += 1

print(c)