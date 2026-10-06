names = ["tarun", "deepak", "anuj", "ankit", "Shashank"]


with open("classmates.txt", "w") as file:
    for name in names:
        file.write(name + "\n")


with open("classmates.txt", "r") as file:
    lines = file.readlines()



print("number of lines:", len(lines))


print("names with more than 5 letters:")

for line in lines:
    print(line)
    name = line.strip()
    if len(name) > 5:
        print(name)