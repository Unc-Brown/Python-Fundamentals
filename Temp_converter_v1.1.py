# ##Temp. Converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5) + 32)
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*(5/9)
    return celsius
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273
    return celsius
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = ((fahrenheit - 32)*(5/9)) + 273
    return kelvin
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = ((kelvin - 273)*(9/5)) + 32
    return fahrenheit


print("--- CELSIUS <--> FAHRENHEIT <--> KELVIN ---")
Q1 = input("Enter value of Temperature: ").strip().lower()
try: Q1_input = float(Q1)
except ValueError: Q1_input = None

if Q1_input:
    What_Unit = input("Enter its unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
    if What_Unit == "c" or "celsius":
        query = input("To what unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
        if query == "kelvin" or query == "k":
            kelvin = celsius_to_kelvin(Q1_input)
            print(f"{kelvin:.1f}")
        elif query == "fahrenheit" or query == "f":
            fahrenheit = celsius_to_fahrenheit(Q1_input)
            print(f"{fahrenheit:.1f}")
        elif query == "c" or query == "celsius":
            print("Already in converted unit!")
    elif What_Unit == "k" or "kelvin":
        query = input("To what unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
        if query == "kelvin" or query == "k":
            kelvin = celsius_to_kelvin(Q1_input)
            print("Already in converted unit!")
        elif query == "fahrenheit" or query == "f":
            fahrenheit = kelvin_to_fahrenheit(Q1_input)
            print(f"{fahrenheit:.1f}")
        elif query == "c" or query == "celsius":
           celsius = kelvin_to_celsius(Q1_input)
           print(f"{celsius:.1f}")
    elif What_Unit == "f" or "fahrenheit":
        query = input("To what unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
        if query == "kelvin" or query == "k":
            kelvin = fahrenheit_to_kelvin(Q1_input)
            print(f"{kelvin:.1f}")
        elif query == "fahrenheit" or query == "f":
           print("Already in converted unit!")
        elif query == "c" or query == "celsius":
            celsius = fahrenheit_to_celsius(Q1_input)
            print(f"{celsius:.1f}")
    elif not What_Unit:
        print("No input!")
    else:
        print("Invalid unit!")