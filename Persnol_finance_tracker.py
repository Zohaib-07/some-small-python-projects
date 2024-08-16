print("Welcome to the Personal Finance Tracker")

class Menu:
    def __init__(self):
        self.income_amount = 0
        self.expense_amount = 0
        self.transactions = []
        self.budget = 0

    def show_menu(self):
        while True:
            x = int(input("What would you like to do(1,2,3,4,5,6)?\n"
                          "1. Add Income\n"
                          "2. Add Expense\n"
                          "3. View Transactions\n"
                          "4. View Summary\n"
                          "5. Set Budget\n"
                          "6. Exit\n"
                          "Enter your choice: "))

            if x == 1:
                self.income()
            elif x == 2:
                self.expenses()
            elif x == 3:
                self.view_transactions()
            elif x == 4:
                self.view_summary()
            elif x == 5:
                self.set_budget()
            elif x == 6:
                print("Exiting the Personal Finance Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please select again.")

    def income(self):
        a = input("Enter 'S' for Salary and 'B' for Bonus: ").upper()
        if a == "S":
            amount = int(input("Enter your Salary Amount: "))
            self.transactions.append({"type": "Income", "category": "Salary", "amount": amount})
        elif a == "B":
            amount = int(input("Enter your Bonus Amount: "))
            self.transactions.append({"type": "Income", "category": "Bonus", "amount": amount})
        else:
            print("Wrong Entry")
            return
        print(f"Income of {amount} added under {a}")

    def expenses(self):
        category = input("Enter the category of the expense (e.g., Food, Rent): ")
        amount = int(input(f"Enter the amount spent on {category}: "))
        self.transactions.append({"type": "Expense", "category": category, "amount": amount})
        print(f"Expense of {amount} added under {category}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded yet.")
        else:
            print("\nTransactions:")
            for transaction in self.transactions:
                print(f"{transaction['type']} - {transaction['category']}: {transaction['amount']}")

    def view_summary(self):
        total_income = sum([t['amount'] for t in self.transactions if t['type'] == "Income"])
        total_expense = sum([t['amount'] for t in self.transactions if t['type'] == "Expense"])
        net_savings = total_income - total_expense

        print("\nSummary:")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expense}")
        print(f"Net Savings: {net_savings}")

    def set_budget(self):
        self.budget = int(input("Enter your monthly budget: "))
        print(f"Budget set to {self.budget}")


menu = Menu()
menu.show_menu()
