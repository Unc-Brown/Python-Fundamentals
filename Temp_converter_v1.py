#This is a temperature converter
print("Temperature Converter")
a = input("Enter value: ")
a_input = float(a) if a else None
if a_input:
    b = input("Enter its unit | Celcius(C), Kelvin(K) or Fahrenheit(F): ")
    if b == "c" or b == "C" or b == "Celcius" or b == "celcius":
        c = input("To What Unit?: ")
        if c == "k" or c == "K" or c == "Kelvin" or c == "kelvin":
            d = a_input+273
            print(f"New temp = {round(d, 2)}{c}")
        elif c == "f" or c == "F" or c == "Fahrenheit" or c == "fahrenheit":
            d = (a_input*(9/5)) + 32
            print(f"New temp = {round(d, 2)}{c}")
        elif c == "c" or c == "C" or c == "Celcius" or c == "celcius":
            print(f"{a_input}{c} stays the same!")
        else:
            print("Cannot convert empty field!")
    
    elif b == "k" or b == "K" or b == "Kelvin" or b == "kelvin":
        c = input("To What Unit?: ")
        if c == "k" or c == "K" or c == "Kelvin" or c == "kelvin":
            print(f"{a_input}{c} stays the same!")
        elif c == "f" or c == "F" or c == "Fahrenheit" or c == "fahrenheit":
            d = ((a_input-273)*(9/5)) + 32
            print(f"New temp = {round(d, 2)}{c}")
        elif c == "c" or c == "C" or c == "Celcius" or c == "celcius":
            d = a_input-273
            print(f"New temp = {round(d, 2)}{c}")
        else:
            print("Cannot convert empty field!")

    elif b == "F" or b == "f" or b == "fahrenheit" or b == "Fahrenheit":
        c = input("To What Unit?: ")
        if c == "k" or c == "K" or c == "Kelvin" or c == "kelvin":
            d = ((a_input-32)*(5/9)) + 273
            print(f"New temp = {round(d, 2)}{c}")
        elif c == "f" or c == "F" or c == "Fahrenheit" or c == "fahrenheit":
            print(f"{a_input}{c} stays the same!")
        elif c == "c" or c == "C" or c == "Celcius" or c == "celcius":
            d = (a_input - 32)*(5/9)
            print(f"New temp = {round(d, 2)}{c}")
        else:
            print("Cannot convert empty field!")
else:
    print("No input value!")
    print("Enter input value!")






