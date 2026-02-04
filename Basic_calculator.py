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
        b = input("Do you wish to switch/change values? (Yes/No): ").lower()
        if b == "yes":
            c = float(input("First number: "))
            d = float(input("Second number: "))
            e = c - d
            print(f"New Difference = {e}")
            while e < 0:
                print("This is still a negative number")
                x = input("Do you still wish to switch/change values again? (Yes/No): ").lower()
                if x == "yes":
                    c = float(input("First number: "))
                    d = float(input("Second number: "))
                    e = c - d
                    print(f"New Difference = {e}")
                elif x == "no":
                    print("Alright then, there you have it!")
                    break
        elif b == "no":
            print("Okay then!")
elif a == "*":
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    product = num1*num2
    print(f"Product = {product}")
elif a == "/":
    while True:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        if num2 != 0:
            division = num1 / num2
            modulus = num1 % num2
            if modulus != 0:
                print(f"{num1}/{num2} = {division} remainder {modulus}")
            else:
                print(f"{num1}/{num2} = {division}")
            break
        else:
            print(f"{num1} cannot be divided by 0")
            choice = input("Do you wish to change numbers? (yes/no): ").lower()
            if choice == "yes":
                continue
            else:
                print(f"Error: {num1} is not divisible by 0")
                break
else:
    print("Invalid Operator!")
    print("Use a valid operator.")