with open("hello.txt", "w") as f:
    f.write("Hi, this file exists!")

filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Sorry, the file does not exist.")

finally:
    print("Finished")