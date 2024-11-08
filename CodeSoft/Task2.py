# Simple Calculator Program

# Function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        # Handle division by zero
        return "Cannot divide by zero!" if num2 == 0 else num1 / num2
    else:
        return "Invalid operation."

# Main program
try:
    # Prompt the user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    
    # Perform calculation and display the result
    result = calculate(num1, num2, operation)
    print(f"The result is: {result}")

except ValueError:
    print("Please enter valid numbers.")
