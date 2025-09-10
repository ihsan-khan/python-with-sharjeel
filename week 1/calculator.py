def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# Regular Division (returns float)
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error! Division by zero.")
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

# Floor Division (returns integer)
def floor_divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error! Division by zero.")
    return x // y

# Ceil Division (returns float)
def ceil_divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error! Division by zero.")
    return -(-x // y)

# Main calculator function
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Divide")
    print("8. Ceil Divide")

    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7/8): ")
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '7':
                print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
            elif choice == '8':
                print(f"{num1} ceil-div {num2} = {ceil_divide(num1, num2)}")
        else:
            print("Invalid Input")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

# Run the calculator
calculator()