def add(a,b):
    return a+b
    pass

def subtract(a,b):

    pass

def multiply(a,b):

    pass

def divide(a,b):
if b == 0:
        return "Error: Division by zero is undefined."
    else:
        return a / b
    pass

def main():
    print("Welcome to the calculator!")
    # Get user inputs for the numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    # Get user input for the operation
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")
    
    # Perform the selected operation
    if operation == '1':
        result = add(a, b)
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = subtract(a, b)
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = multiply(a, b)
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        result = divide(a, b)
        print(f"The result of division is: {result}")
    else:
        print("Invalid operation selected. Please choose 1, 2, 3, or 4.")

# Call the main function
main()
    

