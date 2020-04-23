x = int(input("Enter the value of x:" ))

y = int(input("Enter de value of y:" ))

operation = input("Choose math operation (+, -, *, /: )")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x *y)
elif operation == "/:":
    print(x / y)
else:
    print("You did not provide the correct math operation.")