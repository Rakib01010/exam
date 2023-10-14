class BankAccount:
    totalBalance = 0
    UserAccount = []
    toal_lone=0

    def __init__(self, name, number, password, type=None):
        self.history = []
        self.name = name
        self.number = number
        self.type = type
        self.password = password
        self.account = int(number) + 987654321901
        self.balance = 0
        self.loan_limit = 2

    def delete_account(self, number):
        for account in BankAccount.UserAccount:
            if account["number"] == number:
                BankAccount.UserAccount.remove(account)
                print(f"Account with account number {number} deleted.")
                break
        else:
            print(f"No account found with account number {number}.")
    def create_account(self, name, number, password, type=None):
        account_info = {
            "name": name,
            "number": number,
            "type": type,
            "password": password,
            "account": int(number) + 987654321901,
            "balance": 0,
            "loan_limit": 2,
            "history": []
        }
        BankAccount.UserAccount.append(account_info)
        print(f"Account created: {account_info}")


    def view_all_accounts(self):
        print("All User Accounts:")
        for account in BankAccount.UserAccount:
            print(account)

    def total_available_balance(self):
        print(f"Total Available Balance: {BankAccount.totalBalance}")

    def total_loan_amount(self):
        total=BankAccount.toal_lone
        print(f"Total Loan Amount: {total}")

    def toggle_loan_feature(self, status):
        if status.lower() == "on":
            BankAccount.totalBalance = 0
            print("Loan feature is now ON.")
        elif status.lower() == "off":
            BankAccount.totalBalance = float('inf')
            print("Loan feature is now OFF.")
        else:
            print("Invalid choice. Use 'on' or 'off'.")
    def deposit(self, amount):
        self.balance += amount
        BankAccount.totalBalance+=amount
        self.history.append(f"Deposited: {amount}")
        print(f"Balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            BankAccount.totalBalance -= amount
            self.history.append(f"Withdrew: {amount}")
            print(f"Balance is {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Balance is {self.balance}")

    def view_transaction_history(self):
        for transaction in self.history:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_limit > 0 and self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Took a loan: {amount}")
            self.loan_limit -= 1
            BankAccount.toal_lone+=1
            print(f"Loan of {amount} taken. Remaining loan limit: {self.loan_limit}")
        elif self.balance < amount:
            print("Insufficient funds to take a loan.")
        else:
            print("Loan limit reached.")

    def transfer(self, recipient_number, amount):
        recipient = None
        for account in BankAccount.UserAccount:
            if account["number"] == recipient_number:
                recipient = account
                break
        if recipient:
            if self.balance >= amount:
                recipient["balance"] += amount
                self.balance -= amount
                self.history.append(f"Transferred {amount} to {recipient_number}")
                print(f"Transferred {amount} to {recipient_number}")
            else:
                print("Insufficient funds")
        else:
            print("Recipient account not found.")


def main():
    while True:
        print("\n      1. Create account")
        print("        2. Login")
        print("        3. Exit")
        choice = input("\nSelect an option: ")

        if choice == "1":
            name = input("Name: ")
            number = input("Number: ")
            password = input("Password: ")
            type = input("Type: ")
            user = BankAccount(name, number, password, type)
            BankAccount.UserAccount.append(user.__dict__)
            print(f"Account details: {user.__dict__}")

        elif choice == "2":
            auth= input("User of admin(Input will be User or Admin and you can use any of your account as a admin accout): ")
            if auth == "User" or "user":
                name = input("Name: ")
                password = input("Password: ")
                logged_user = None
                for account in BankAccount.UserAccount:
                    if account["name"] == name and account["password"] == password:
                        logged_user = account
                        break
                if logged_user:
                    user = BankAccount(logged_user["name"], logged_user["number"], logged_user["password"],
                                       logged_user["type"])
                    while True:
                        print("\n      1. Deposit")
                        print("        2. Withdraw")
                        print("        3. Check Balance")
                        print("        4. View Transaction History")
                        print("        5. Take Loan")
                        print("        6. Transfer")
                        print("        7. Exit")
                        user_choice = input("\nSelect an option: ")

                        if user_choice == "1":
                            amount = float(input("Enter deposit amount: "))
                            user.deposit(amount)
                        elif user_choice == "2":
                            amount = float(input("Enter withdrawal amount: "))
                            user.withdraw(amount)
                        elif user_choice == "3":
                            user.check_balance()
                        elif user_choice == "4":
                            user.view_transaction_history()
                        elif user_choice == "5":
                            amount = float(input("Enter loan amount: "))
                            user.take_loan(amount)
                        elif user_choice == "6":
                            recipient_number = input("Enter recipient's number: ")
                            amount = float(input("Enter transfer amount: "))
                            user.transfer(recipient_number, amount)
                        elif user_choice == "7":
                            print("Exiting user menu...")
                            break
                        else:
                            print("Invalid choice.")
                else:
                    print("Invalid credentials.")
            elif auth == "Admin" or "admin":
                name = input("Name: ")
                password = input("Password: ")
                logged_user = None
                for account in BankAccount.UserAccount:
                    if account["name"] == name and account["password"] == password:
                        logged_user = account
                        break
                if logged_user:
                    user = BankAccount(logged_user["name"], logged_user["number"], logged_user["password"],
                                       logged_user["type"])
                    while True:
                        print("\n      1. create account")
                        print("        2. delete accout")
                        print("        3. see all user accounts")
                        print("        4. total available balance")
                        print("        5. total loan amount")
                        print("        6.  loan feature of")
                        print("        7. Exit")
                        user_choice = input("\nSelect an option: ")

                        if user_choice == "1":
                            name = input("Name: ")
                            number = input("Number: ")
                            password = input("Password: ")
                            type = input("Type: ")
                            user = BankAccount(name, number, password, type)
                            BankAccount.UserAccount.append(user.__dict__)
                            print(f"Account details: {user.__dict__}")
                        elif user_choice == "2":
                            number = input("Give accout number: ")
                            user.delete_account(number)
                        elif user_choice == "3":
                            user.view_all_accounts()
                        elif user_choice == "4":
                            user.total_available_balance()
                        elif user_choice == "5":
                            user.total_loan_amount()
                        elif user_choice == "6":
                            user.toggle_loan_feature("On")
                        elif user_choice == "7":
                            print("Exiting user menu...")
                            break
                        else:
                             print("Invalid choice.")

        else:
            print("No")





if __name__ == "__main__":
    main()
