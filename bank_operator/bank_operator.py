from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if len(users) < 1 :
        print('List Empty')
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    list_users()
    amount = 0
    if len(users) < 1 :
        print("No users available. Please create a user first.")
        return
    idx = int(input("Select user number: ")) - 1
    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    account_choice = int(input("Enter your choice (1, 2, 3): "))
    
    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        print("Invalid account type!")
        return

    amount += float(input("Enter initial deposit: "))

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    list_users()
    if len(users) == 0:
        return
    idx = int(input("Select user: ")) - 1
    if idx - 1 > len(users):
        print("Invalid user selection.\n")
        return
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to deposit: "))  # Fixed bug
    user.accounts2[acc_idx].deposit(amount)

def withdraw_money():
    list_users()
    if len(users) == 0:
        return
    idx = int(input("Select user: ")) - 1
    if idx - 1 > len(users):
        print("Invalid user selection.\n")
        return
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to withdraw: "))
    try:
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    if len(users) < 1 :
        print('No Users Were Found')
        return
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            print(tx)

