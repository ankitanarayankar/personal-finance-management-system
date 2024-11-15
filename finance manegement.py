# Personal Finance Management System

class PersonalFinance:
    def __init__(self):
        self.income = []
        self.expenses = []

    def add_income(self, source, amount):
        self.income.append({"source": source, "amount": amount})
        print(f"Income of {amount} from {source} added.")

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        print(f"Expense of {amount} for {category} added.")

    def total_income(self):
        return sum(item['amount'] for item in self.income)

    def total_expenses(self):
        return sum(item['amount'] for item in self.expenses)

    def balance(self):
        return self.total_income() - self.total_expenses()

    def summary(self):
        print("\n--- Income Summary ---")
        for item in self.income:
            print(f"Source: {item['source']}, Amount: {item['amount']}")

        print("\n--- Expense Summary ---")
        for item in self.expenses:
            print(f"Category: {item['category']}, Amount: {item['amount']}")

        print("\n--- Financial Overview ---")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expenses: {self.total_expenses()}")
        print(f"Current Balance: {self.balance()}")


# Main Program
finance = PersonalFinance()

# Sample data
finance.add_income("Salary", 50000)
finance.add_income("Freelancing", 15000)

finance.add_expense("Rent", 20000)
finance.add_expense("Groceries", 5000)
finance.add_expense("Entertainment", 3000)

# Displaying Summary
finance.summary()
