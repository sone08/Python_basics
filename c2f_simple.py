# Temperature conversion example
while True:
    temp = input("Enter temperature in celsius (or q to quit): ")
    if temp.lower() == 'q':
        print("Exiting temperature conversion.")
        break  # Exit loop
    try:
        temp_c = float(temp)
        temp_f = (temp_c * 9 / 5) + 32
        print(f"{temp_c}°C is {temp_f:.2f}°F")
    except ValueError:
        print("please enter a valid number.")
        break  # Exit loop on invalid input