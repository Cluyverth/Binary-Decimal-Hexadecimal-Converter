def menu(): #? create a menu function

    print("""
    1. Convert Binary to Decimal
    2. Convert Decimal to Binary
    3. Exit
    """)

while True: #? create a while loop to keep the program running

    menu()  #? call the menu function
    choice = input("Enter your choice: ")   #? ask the user to choose an option
    if choice == "1":
        print("Binary to Decimal")
        binary = input("Enter a binary number: ")
        print(f"The decimal value of {binary} is {int(binary, 2)}") #? convert the binary number to decimal
    elif choice == "2":
        print("Decimal to Binary")
        decimal = int(input("Enter a decimal number: "))
        print(f"The binary value of {decimal} is {bin(decimal)[2:]}")   #? convert the decimal number to binary
    elif choice == "3":
        print("Exit")   #? exit the program
        break
    else:
        print("Invalid choice") #! if the user enters an invalid choice, tell them to try again
        continue
    print("\n")
    choice = input("Continue? (y/n): ") #? ask the user if they want to continue
    if choice == "y":   #? if the user enters y, continue
        continue
    else:   #? if the user enters n, exit the program
        print("Bye")
        break