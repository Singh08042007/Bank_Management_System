import utils

def add():
    amount = int(input("Enter amount to deposit: "))
    utils.balance += amount
    utils.transactions.append(f"Deposited: {amount}")
    print(f"Deposited Successfully: {amount}")