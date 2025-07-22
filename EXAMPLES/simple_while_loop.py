i = 0
while i < 5:
    print("i is:", i)
    i += 1

print("Loop finished")

print("Welcome to ticket sales\n")
while True: # Loop "forever"

    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break # Exit loop
    quantity = int(raw_quantity) # could validate via try/except
    print(f"sending {quantity} ticket(s)")
    break # Exit loop after one iteration


# Temperature conversion example
while True:
    raw_temp = input("Enter temperature in Fahrenheit (or q to quit): ")
    if raw_temp.lower() == 'q':
        print("Exiting temperature conversion.")
        break  # Exit loop
    try:
        temp_f = float(raw_temp)
        temp_c = (temp_f - 32) * 5 / 9
        print(f"{temp_f}°F is {temp_c:.2f}°C")
    except ValueError:
        print("Please enter a valid number.")
        break  # Exit loop on invalid input


    
