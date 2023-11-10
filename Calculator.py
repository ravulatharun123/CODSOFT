def calculator_menu():
    while True:
        print("\n*** Calculator Menu ***")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        option = input("Enter operation (1/2/3/4/5): ")

        if option == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif option == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif option == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif option == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        elif option == '5':
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid Option. Please choose a valid operation (1/2/3/4/5).")

calculator_menu_input = input("Do you want to use the Calculator? (yes/no): ").strip().lower()
if calculator_menu_input == "yes":
    calculator_menu()
