def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Enter a valid number!")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Modulus")

choice = input("Enter choice: ")

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
elif choice == "5":
    print("Result:", num1 ** num2)
elif choice == "6":
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")