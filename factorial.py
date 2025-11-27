import math

def calculate_factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return math.factorial(n)

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate factorials
factorial1 = calculate_factorial(num1)
factorial2 = calculate_factorial(num2)

# Display results
print(f"\nFactorial of {num1} = {factorial1}")
print(f"Factorial of {num2} = {factorial2}")


#changes by bindu
print("\nchanges made by bindu")
