import utils

def withdraw():
    amount = int(input("Enter amount to withdraw: "))

    if amount <= utils.balance:
        utils.balance -= amount
        utils.transactions.append(f"Withdrawn: {amount}")
        print("Withdraw successful")
    else:
        print("Insufficient balance")