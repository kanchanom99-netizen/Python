# Calculator Program

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("% for Modulus")
    print("** for Power")

    op = input("Enter operation: ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero")
            result = None
        else:
            result = a / b
    elif op == "%":
        if b == 0:
            print("Cannot find modulus with zero")
            result = None
        else:
            result = a % b
    elif op == "**":
        result = a ** b
    else:
        print("Invalid operation")
        result = None

    if result is not None:
        print("Result =", result)

except ValueError:
    print("Invalid input. Please enter numbers only.")
