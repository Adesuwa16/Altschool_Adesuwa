from Expense_Classes import Expense, ExpenseDb

# Create an expense
expense1 = Expense("Lunch", 15.50)

# Create an ExpenseDB instance
db = ExpenseDb()
db.add_expense(expense1)

# Print all expenses
print(db.to_dict())
