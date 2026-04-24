from deposit import add
from show_balance import show
from withdraw import withdraw
from statement import show_statement

def bank():
    while True:
        print("\n------ Welcome to the Bank ------")
        print("1. Deposit Amount")
        print("2. Show Balance")
        print("3. Withdraw Balance")
        print("4. Show Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Please enter a valid number!")
            continue

        choice = int(choice)

        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            show_statement()
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid Choice")

bank()