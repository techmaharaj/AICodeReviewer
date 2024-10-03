# addition.py

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers and return the result.

    Args:
        a (float): The first number to add.
        b (float): The second number to add.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def main():
    """
    Main function to take user input and print the result of adding two numbers.
    """
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform addition
        result = add_numbers(num1, num2)

        # Display result
        print(f"The result of adding {num1} and {num2} is {result:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
