class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        if isinstance(balance, (int, float)):
            if balance >= 0:
                self.__balance = balance
            else:
                raise ValueError("Initial balance must be a non-negative number.")
        else:
            raise ValueError("Balance must be a number.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_account_info(self):
        print("Account Number:", self.__account_number)
        print("Current Balance:", self.__balance)

    def __display_balance(self):
        print("Current Balance:", self.__balance)

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if isinstance(balance, (int, float)):
            if balance >= 0:
                self.__balance = balance
                print("Balance updated successfully.")
            else:
                print("Error: Balance must be a non-negative number.")
        else:
            print("Error: Balance must be a number.")

if __name__ == "__main__":
    account = BankAccount("123456789", 1000.0)
    account.deposit(500.0)
    account.withdraw(300.0)
    account.set_balance(-200.0)
    account.display_account_info()
    print("Account Number (Getter):", account.get_account_number())
    print("Balance (Getter):", account.get_balance())
