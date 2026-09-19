#AssignmentT # 01
#Calculator (homework) Nested condition

Num1 = int(input("Enter your first number: "))

Operator = input("Enter your operator (+,-,*,/): ")

Num2 = int(input("Enter your second number: "))

if Operator =="+":
   print(Num1+Num2)

elif Operator =="-":
    print(Num1-Num2)

elif Operator =="*":
    print(Num1*Num2)

elif Operator =="/":
    if Num2 != 0:
      print(Num1/Num2)
    else:
      print("Sorry, zero division is not allowed in python")
else:
    print("Invalid operator")
