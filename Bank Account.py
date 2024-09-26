class BankAccount:
    def _init_(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully. New balance is: {self.balance}")
        else:
            print("Invalid deposit amount!")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal failed.")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. New balance is: {self.balance}")
    def check_balance(self):
        print(f"Account Balance for {self.name}: {self.balance}")
def create_account(accounts):
    name = input("Enter account holder's name: ")
    account_number = input("Enter a new account number: ")
    initial_balance = float(input("Enter initial deposit amount: "))
    account = BankAccount(name, account_number, initial_balance)
    accounts[account_number] = account
    print(f"Account created for {name} with balance {initial_balance}\n")
def bank_system():
    accounts = {}
    
    while True:
        print("\n--- Bank System Menu ---")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account(accounts)
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found!")
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found!")
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found!")
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice, please try again.")
bank_system()
