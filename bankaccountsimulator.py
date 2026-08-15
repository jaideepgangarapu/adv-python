balance = 0
transactions = []


def deposit():
    global balance

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount. The amount must be greater than 0.")
            return

        balance += amount
        transactions.append({
            "type": "deposit",
            "amount": amount
        })

        print(f"Rs{amount:.2f} successfully deposited.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount. The amount must be greater than 0.")
            return

        if amount > balance:
            print("Insufficient balance. Please enter a valid amount.")
            return

        balance -= amount
        transactions.append({
            "type": "withdraw",
            "amount": amount
        })

        print(f"Rs{amount:.2f} successfully withdrawn.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def check_balance():
    print(f"Current balance: Rs{balance:.2f}")


def show_history():
    if not transactions:
        print("No transactions yet.")
        return

    print("\n----- Transaction History -----")

    for i, transaction in enumerate(transactions, start=1):
        transaction_type = transaction["type"]
        amount = transaction["amount"]

        print(f"{i}. {transaction_type.capitalize():8} : Rs{amount:.2f}")


def main():
    while True:
        print("\n----- Bank Account Simulator -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            deposit()

        elif choice == "2":
            withdraw()

        elif choice == "3":
            check_balance()

        elif choice == "4":
            show_history()

        elif choice == "5":
            print("Thank you for using the Bank Account Simulator.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()