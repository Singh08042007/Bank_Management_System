import utils

def add():
    amount = int(input("Enter amount to deposit: "))
    utils.balance += amount
    print(f"Deposited Successfully: {amount}")