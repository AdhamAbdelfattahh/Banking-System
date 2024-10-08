import getpass

class BankAccount:
    def __init__(self, account_holder, password):
        self.account_holder = account_holder
        self.password = password
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, password):
        if account_holder in self.accounts:
            print("Account already exists.")
            return False
        else:
            self.accounts[account_holder] = BankAccount(account_holder, password)
            print("Account created successfully.")
            return True

    def authenticate(self, account_holder, password):
        account = self.accounts.get(account_holder)
        if account and account.password == password:
            return account
        else:
            print("Authentication failed. Check your account holder or password.")
            return None


def main():
    banking_system = BankingSystem()

    while True:
        print("\nSelect an option:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            account_holder = input("Enter your name: ")
            password = getpass.getpass("Create a password: ")
            banking_system.create_account(account_holder, password)
        elif choice == '2':
            account_holder = input("Enter your name: ")
            password = getpass.getpass("Enter your password: ")
            account = banking_system.authenticate(account_holder, password)

            if account:
                while True:
                    print("\nSelect an option:")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. View Transaction History")
                    print("5. Logout")

                    user_choice = input("Enter your choice (1/2/3/4/5): ")

                    if user_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif user_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif user_choice == '3':
                        account.check_balance()
                    elif user_choice == '4':
                        account.view_transaction_history()
                    elif user_choice == '5':
                        print("Logging out.")
                        break
                    else:
                        print("Invalid Input")
        elif choice == '3':
            print("Exiting the Banking System.")
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
