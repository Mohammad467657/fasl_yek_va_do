# ===============================
# Simple Calculator
# ===============================

import math

def show_menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Absolute Value (abs)")
    print("6. Power (x^y)")
    print("7. Square Root (√x)")
    print("0. Exit")

def get_number(message):
    while True:
        try:
            return float(input(message))
        except:
            print("Invalid input, please enter a number.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    # Exit
    if choice == "0":
        print("Goodbye 👋")
        break

    # Addition
    elif choice == "1":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result =", a + b)

    # Subtraction
    elif choice == "2":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result =", a - b)

    # Multiplication
    elif choice == "3":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result =", a * b)

    # Division
    elif choice == "4":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        if b == 0:
            print("Error: Division by zero!")
        else:
            print("Result =", a / b)

    # Absolute Value
    elif choice == "5":
        a = get_number("Enter a number: ")
        print("Result =", abs(a))

    # Power
    elif choice == "6":
        a = get_number("Enter base: ")
        b = get_number("Enter exponent: ")
        print("Result =", pow(a, b))

    # Square Root
    elif choice == "7":
        a = get_number("Enter a number: ")
        if a < 0:
            print("Error: Cannot calculate square root of negative number")
        else:
            print("Result =", math.sqrt(a))

    else:
        print("Invalid choice, please try again.")
