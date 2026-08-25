# Simple Calculator

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice = input("Enter your choice (1-5): ")

# Perform the selected operation
if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", result)

elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)

elif choice == "5":
    if num2 == 0:
        print("Error: Cannot perform modulus with zero.")
    else:
        result = num1 % num2
        print("Result:", result)

else:
    print("Invalid choice.")