#Assignment # 02
# Temperature Converter
# This program converts Celsius to Fahrenheit
# and Fahrenheit to Celsius.

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Ask the user to choose a conversion type
choice = input("Enter your choice (1 or 2): ")

# Take temperature input from the user
temperature = float(input("Enter the temperature: "))

# Convert Celsius to Fahrenheit
if choice == "1":
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"{temperature}°C = {fahrenheit:.2f}°F")

# Convert Fahrenheit to Celsius
elif choice == "2":
    celsius = (temperature - 32) * 5 / 9
    print(f"{temperature}°F = {celsius:.2f}°C")

# Handle an invalid choice
else:
    print("Invalid choice. Please select 1 or 2.")
