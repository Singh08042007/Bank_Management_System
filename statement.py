import utils

def show_statement():
    print("\n--- Transaction Statement ---")
    
    if len(utils.transactions) == 0:
        print("No transactions yet.")
    else:
        for t in utils.transactions:
            print(t)