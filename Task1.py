def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Converter")
    print("Choose the unit of the temperature you want to convert:")
    print("1. Celsius (C)")
    print("2. Fahrenheit (F)")
    print("3. Kelvin (K)")

    unit_choice = input("Enter the number corresponding to your choice (1/2/3): ")
    temperature = float(input("Enter the temperature value: "))

    if unit_choice == '1':  # Celsius
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} °C = {fahrenheit:.2f} °F")
        print(f"{temperature} °C = {kelvin:.2f} K")

    elif unit_choice == '2':  # Fahrenheit
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} °F = {celsius:.2f} °C")
        print(f"{temperature} °F = {kelvin:.2f} K")

 ⬤