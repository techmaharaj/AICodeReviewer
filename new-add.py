while True:
    try:
        first_number = int(input("Enter the first number (or type exit to quit): "))
        second_number = int(input("Enter the second number (or type exit to quit): "))
        break
    except ValueError:
        print("Please enter valid numbers.")

total = first_number + second_number
print(f"Sum is: {total}")
