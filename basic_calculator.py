
while True:
    
    print(f"\n- - - MENU - - -")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    try:
        choice = int(input(("Select an operation (1-5): ")))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 5:
        print("Exiting the system as requested, see you...")
        break

    if choice in [1, 2 , 3 , 4]:    
        try:
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))
        except ValueError:
            print("Invalid input! Please enter numeric value (int, float): ")
            continue

        if choice == 4:
            if num1 == 0 and num2 == 0:
                print("*! EROR !* 0/0 is undefined.")
                while num1 == 0 and num2 == 0:
                    num1 = int(input("Enter the 1st number again for division: "))
                    num2 = int(input("Enter the 2nd number again for division: "))
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif num2 == 0:
                print("*! EROR !* The denominator cannot be zero.")
                while num2 == 0:
                    num2 = int(input("Enter the 2nd number again for division (non-zero): "))
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
    
        if choice == 1:
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            show_absolute = str(input("Would you like to see the absolute value (Yes - No): ")).capitalize()
            print(f"Result: {num1} - {num2} = {num1 - num2}")
            if show_absolute == "Evet":
                print(f"Absolute value: {abs(num1 - num2)}")
            elif show_absolute != "Evet":
                print("Absolute value not showed as requested.")
        elif choice == 3:
            print(f"Result: {num1} X {num2} = {num1 * num2}")
    else:
        print("Invalid input! Please enter a value between 1 and 5.")
         
    
        
