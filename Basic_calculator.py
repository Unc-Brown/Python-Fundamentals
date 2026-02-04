#This is a calculator!
print("BASIC CALCULATOR!!")
a = input("Enter an operator sign; plus(+), minus(-), multiplication(*) or division(/): ")
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
        if b == "Yes".lower():
            c = float(input("First number: "))
            d = float(input("Second number: "))
            e = c - d
            print(f"New Difference = {e}")
            while e < 0:
                print("This is still a negative number")
                x = input("Do you still wish to switch/change values again? (Yes/No): ")
                if x == "Yes".lower():
                    c = float(input("First number: "))
                    d = float(input("Second number: "))
                    e = c - d
                    print(f"New Difference = {e}")
                elif x == "No" or x == "no":
                    print("Alright then, there you have it!")
                    break
        elif b == "No".lower():
            print("Okay then!")
elif a == "*":
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    product = num1*num2
    print(f"Product = {product}")
elif a == "/":
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    while num2 == 0:
        print(f"{num1} can not be divided by 0")
        query = input("Do you wish to change numbers: ")
        if query == "Yes".lower():
            num1_ = float(input("First number: "))
            num2_ = float(input("Second number: "))
            division = num1_/num2_
            modulus = num1_%num2_
            if not modulus == 0:
                print(f"{num1_}/{num2_} = {round(division)} remainder {modulus}")
            else:
                print(f"{num1_}/{num2_} = {round(division)}")
        if query == "No".lower():
            print(f"Error: {num1} is not divisible by 0")
        break
else:
    print("Invalid Operator!")
    print("Use a valid operator.")
