# ##Temp. Converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5) + 32)
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*(5/9)
    return celsius
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = ((fahrenheit - 32)*(5/9)) + 273.15
    return kelvin
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = ((kelvin - 273)*(9/5)) + 32
    return fahrenheit


print("--- CELSIUS <--> FAHRENHEIT <--> KELVIN ---")
Q1 = input("Enter value of Temperature: ").strip().lower()
if not Q1.isdigit():
    print("--No strings allowed (a,b,c or *_-'@)--")
elif Q1.isdigit():
    Q1_input = float(Q1) if Q1 else None
    if Q1_input:
        What_Unit = input("Enter its unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
        if What_Unit == "c" or What_Unit == "celsius":
            query = input("To what unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
            if query == "kelvin" or query == "k":
                kelvin = celsius_to_kelvin(Q1_input)
                print(f"Temperaure: {kelvin:.1f}K")
            elif query == "fahrenheit" or query == "f":
                fahrenheit = celsius_to_fahrenheit(Q1_input)
                print(f"Temperaure: {fahrenheit:.1f}°F")
            elif query == "c" or query == "celsius":
                print("Already in converted unit!")
        elif What_Unit == "k" or "kelvin":
            query = input("To what unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
            if query == "kelvin" or query == "k":
                print("Already in converted unit!")
            elif query == "fahrenheit" or query == "f":
                fahrenheit = kelvin_to_fahrenheit(Q1_input)
                print(f"Temperaure: {fahrenheit:.1f}°F")
            elif query == "c" or query == "celsius":
                celsius = kelvin_to_celsius(Q1_input)
                print(f"Temperaure: {celsius:.1f}°C")
        elif What_Unit == "f" or "fahrenheit":
            query = input("To what unit | (K)elvin - (C)elsius - (F)ahrenheit: ").lower()
            if query == "kelvin" or query == "k":
                kelvin = fahrenheit_to_kelvin(Q1_input)
                print(f"Temperaure: {kelvin:.1f}K")
            elif query == "fahrenheit" or query == "f":
                print("Already in converted unit!")
            elif query == "c" or query == "celsius":
                celsius = fahrenheit_to_celsius(Q1_input)
                print(f"Temperaure: {celsius:.1f}°C")
        elif not What_Unit:
            print("No input!")
        else:
            print("Invalid unit!")