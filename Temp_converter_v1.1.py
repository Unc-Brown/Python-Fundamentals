# ##Temp. Converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5) + 32)
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*(5/9)
    return celsius

print("CELSIUS --> FAHRENHEIT <->")
a = input("What conversion [to (C or F)]: ").lower()
if a == "c" or a == "celsius":
    q = float(input("Enter temp in celsius: "))
    conversion = celsius_to_fahrenheit(q)
    print(f"{conversion} Fahrenheit")
elif a == "f" or a == "fahrenheit":
    q = float(input("Enter temp in fahrenheit: "))
    conversion = fahrenheit_to_celcius(q)
    print(f"{conversion:.1f} Celsius")
