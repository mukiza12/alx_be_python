# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("🌡️ Temperature Conversion Tool")
    temp_input = input("Enter the temperature value: ")

    try:
        temperature = float(temp_input)  # ✅ Validate numeric input
    except ValueError:
        raise ValueError("❌ Invalid temperature. Please enter a numeric value.")

    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"✅ {temperature}°C is equal to {converted_temp:.2f}°F.")
    elif unit == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"✅ {temperature}°F is equal to {converted_temp:.2f}°C.")
    else:
        print("❌ Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
