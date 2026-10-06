def read_marks_file(filename):
    try:
        with open(filename, "r") as file:
            marks = int(file.read())
            print("Marks:", marks)

    except FileNotFoundError:
        print(f"File not found: {filename}")

    except ValueError:
        print(f"The contents of {filename} were not a number.")

    finally:
        print("File operation finished.")


# Create the test files

with open("hello.txt", "w") as file:
    file.write("hello")

with open("marks75.txt", "w") as file:
    file.write("75")


# D2: Test all three situations

print("Test 1:")
read_marks_file("missing.txt")

print("\nTest 2:")
read_marks_file("hello.txt")

print("\nTest 3:")
read_marks_file("marks75.txt")