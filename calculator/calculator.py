def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Welcome to the Python Calculator by Emmanuel Naweji at T2S!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            # Get the operation
            operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ").strip()
            
            if operation.lower() == 'q':
                print("Goodbye!")
                break

            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please try again.")
                continue

            # Get the numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the calculation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print(f"The result is: {result}")
        
        except ValueError:
            print("Invalid input. Please use only numeric values.")
            
# Running the calculator
if __name__ == "__main__":
    calculator()