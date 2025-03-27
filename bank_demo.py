# ATM application, Account information will be kept (dict), menu money withdrawal deposit balance query, if the amount to be withdrawn is not in the account, the additional account will be asked to be used

def main():
    account = {
        # My full name is Ali JAMIL
        "name": "Ali JAMIL",
        "balance": 1000,
        "additional_account": 500
    }

    def display_menu():
        print("\nATM Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

    def deposit_money():
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            account["balance"] += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw_money():
        amount = float(input("Enter amount to withdraw: "))
        if amount <= account["balance"]:
            account["balance"] -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            deficit = amount - account["balance"]
            use_additional = input(f"Insufficient balance. Use additional account for ${deficit}? (yes/no): ").lower()
            if use_additional == "yes" and deficit <= account["additional_account"]:
                account["additional_account"] -= deficit
                account["balance"] = 0
                print(f"${amount} withdrawn successfully using additional account.")
            else:
                print("Transaction failed. Insufficient funds.")

    def check_balance():
        print(f"Main Account Balance: ${account['balance']}")
        print(f"Additional Account Balance: ${account['additional_account']}")

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            deposit_money()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()