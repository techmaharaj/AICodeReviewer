while True:
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Please enter valid numbers.")

sum = first_number + second_number
print(f"Sum is: {sum}")
