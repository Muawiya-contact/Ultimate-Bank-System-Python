class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = max(balance, 0)  # Ensures balance is not negative
        print(f"\n✅ Account for {self.account_holder} created successfully! 🏦")
        self.get_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"💰 Successfully deposited ${amount} | New Balance: ${self.__balance}")
        else:
            print("❌ Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds!")
        elif amount <= 0:
            print("❌ Invalid withdrawal amount!")
        else:
            self.__balance -= amount
            print(f"💸 Withdrawn: ${amount} | Remaining Balance: ${self.__balance}")

    def get_balance(self):
        print(f"📊 Current Balance for {self.account_holder}: ${self.__balance}")

# 🏦 Bank System Menu
def main():
    print("\n🌟 Welcome to the Ultimate Bank System! 🌟")

    name = input("👤 Enter Account Holder's Name: ")
    initial_balance = int(input("💵 Enter Initial Balance (or 0): "))

    account = BankAccount(name, initial_balance)

    while True:
        print("\n📌 MAIN MENU")
        print("1️⃣ Deposit")
        print("2️⃣ Withdraw")
        print("3️⃣ Check Balance")
        print("4️⃣ Exit")

        try:
            choice = int(input("👉 Enter your choice: "))

            if choice == 1:
                amount = int(input("💰 Enter amount to deposit: "))
                account.deposit(amount)

            elif choice == 2:
                amount = int(input("💸 Enter amount to withdraw: "))
                account.withdraw(amount)

            elif choice == 3:
                account.get_balance()

            elif choice == 4:
                print("👋 Thank you for using Ultimate Bank System! See you again!")
                break

            else:
                print("❌ Invalid choice! Please enter a valid option.")

        except ValueError:
            print("❌ Error! Please enter a valid number.")

if __name__ == "__main__":
    main()
