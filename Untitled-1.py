def reverse_number(n):
    reversed_num = 0
    while n > 0:
        remainder = n % 10
        reversed_num = (reversed_num * 10) + remainder
        n = n // 10
    return reversed_num

# Get input from the user
try:
    num = int(input("Enter a whole number: "))
    if num < 0:
        print("Please enter a non-negative whole number.")
    else:
        print(f"Reversed number: {reverse_number(num)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")