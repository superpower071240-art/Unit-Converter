history_file = "history.txt"

def save_history(text):
    with open(history_file, "a") as file:
        file.write(text + "\n")

while True:
    print("\n===== ADVANCED UNIT CONVERTER =====")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Area Converter")
    print("5. Volume Converter")
    print("6. View History")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # LENGTH
    if choice == "1":
        print("\n1. Meter to Kilometer")
        print("2. Kilometer to Meter")
        print("3. Inch to Centimeter")
        print("4. Feet to Meter")

        sub = input("Choose: ")

        if sub == "1":
            m = float(input("Enter meters: "))
            result = m / 1000
            text = f"{m} m = {result} km"

        elif sub == "2":
            km = float(input("Enter kilometers: "))
            result = km * 1000
            text = f"{km} km = {result} m"

        elif sub == "3":
            inch = float(input("Enter inches: "))
            result = inch * 2.54
            text = f"{inch} inch = {result} cm"

        elif sub == "4":
            feet = float(input("Enter feet: "))
            result = feet * 0.3048
            text = f"{feet} ft = {round(result,2)} m"

        else:
            print("Invalid Choice")
            continue

        print(text)
        save_history(text)

    # WEIGHT
    elif choice == "2":
        print("\n1. Gram to Kilogram")
        print("2. Kilogram to Gram")
        print("3. Kilogram to Pound")

        sub = input("Choose: ")

        if sub == "1":
            g = float(input("Enter grams: "))
            result = g / 1000
            text = f"{g} g = {result} kg"

        elif sub == "2":
            kg = float(input("Enter kilograms: "))
            result = kg * 1000
            text = f"{kg} kg = {result} g"

        elif sub == "3":
            kg = float(input("Enter kilograms: "))
            result = kg * 2.20462
            text = f"{kg} kg = {round(result,2)} lb"

        else:
            print("Invalid Choice")
            continue

        print(text)
        save_history(text)

    # TEMPERATURE
    elif choice == "3":
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")

        sub = input("Choose: ")

        if sub == "1":
            c = float(input("Enter Celsius: "))
            result = (c * 9/5) + 32
            text = f"{c}°C = {round(result,2)}°F"

        elif sub == "2":
            f = float(input("Enter Fahrenheit: "))
            result = (f - 32) * 5/9
            text = f"{f}°F = {round(result,2)}°C"

        elif sub == "3":
            c = float(input("Enter Celsius: "))
            result = c + 273.15
            text = f"{c}°C = {round(result,2)} K"

        else:
            print("Invalid Choice")
            continue

        print(text)
        save_history(text)

    # AREA
    elif choice == "4":
        print("\n1. Square Meter to Square Kilometer")
        print("2. Acre to Square Meter")

        sub = input("Choose: ")

        if sub == "1":
            sqm = float(input("Enter square meters: "))
            result = sqm / 1000000
            text = f"{sqm} sq.m = {result} sq.km"

        elif sub == "2":
            acre = float(input("Enter acres: "))
            result = acre * 4046.86
            text = f"{acre} acre = {round(result,2)} sq.m"

        else:
            print("Invalid Choice")
            continue

        print(text)
        save_history(text)

    # VOLUME
    elif choice == "5":
        print("\n1. Liter to Milliliter")
        print("2. Milliliter to Liter")

        sub = input("Choose: ")

        if sub == "1":
            l = float(input("Enter liters: "))
            result = l * 1000
            text = f"{l} L = {result} mL"

        elif sub == "2":
            ml = float(input("Enter milliliters: "))
            result = ml / 1000
            text = f"{ml} mL = {result} L"

        else:
            print("Invalid Choice")
            continue

        print(text)
        save_history(text)

    # HISTORY
    elif choice == "6":
        try:
            with open(history_file, "r") as file:
                print("\n===== CONVERSION HISTORY =====")
                print(file.read())
        except FileNotFoundError:
            print("No history found.")

    # EXIT
    elif choice == "7":
        print("Thank you for using Advanced Unit Converter!")
        break

    else:
        print("Invalid Choice! Try Again.")