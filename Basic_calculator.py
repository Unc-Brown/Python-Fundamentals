import math

#This is a calculator!
print("BASIC CALCULATOR!!")
a = input("Enter an operator sign; plus(+), minus(-), multiplication(*) or division(/): ")
    # b = input("Enter an operator sign; plus(+), minus(-), multiplication(*) or division(/): ")
    # if b != "+" or "-" or "/" or "*":
    #     print("Dumbass!!")
if a == "+":
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    sum = num1 + num2
    print(f"Sum = {sum}")
elif a == "-":
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    diff = num1 - num2
    print(f"Difference = {diff}")
    if diff<0:
        print("This is a negative number")
        b = input("Do you wish to switch/change values? (Yes/No): ")
        if b == "Yes" or b == "yes":
            c = float(input("First number: "))
            d = float(input("Second number: "))
            e = c - d
            print(f"New Difference = {e}")
            if e < 0:
                print("This is still a negative number")
                x = input("Do you still wish to switch/change values again? (Yes/No): ")
                if x == "Yes" or x == "yes":
                    c = float(input("First number: "))
                    d = float(input("Second number: "))
                    e = c - d
                    print(f"New Difference = {e}")
                elif x == "No" or x == "no":
                    print("Alright then, there you have it!")
        elif b == "No" or b == "no":
            print("Okay then!")
elif a == "*":
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    product = num1*num2
    print(f"Product = {product}")
elif a == "/":
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    division = num1/num2
    modulus = num1%num2
    print(f"{num1}/{num2} = {round(division)} remainder {modulus}")
else:
    print("Invalid Operator!")
    print("Use a valid operator.")
