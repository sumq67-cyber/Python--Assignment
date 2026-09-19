#Assignment # 03
# menu driven calculator
again = 'yes'
while again.lower() == 'yes':
    try:
        print("\n=== Menu-Driven Calculator ===")
        Num1 = float(input("Enter your first number: "))
        Operator = input("Enter your operator (+,-,*,/): ")
        Num2 = float(input("Enter your second number: "))

        if Operator == "+":
            print(Num1 + Num2)

        elif Operator == "-":
            print(Num1 - Num2)

        elif Operator == "*":
            print(Num1 * Num2)

        elif Operator == "/":
            if Num2 != 0:
                print(Num1 / Num2)
            else:
                print("Sorry, zero division is not allowed.")
        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    again = input("Do you want to calculate again? (yes/no): ")

print("Thank you for using the Calculator!")
