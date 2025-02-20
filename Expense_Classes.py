##Expense Class
import uuid
from datetime  import datetime, timezone


class Expense:
    def __init__(self,title, amount):
        self.id = uuid.uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def update(self, title=None, amount=None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

#ExpenseDatabase Class
class ExpenseDb:
    def __init__(self):
        self.expenses = {}
    
    def add_expense(self, expense):
        self.expenses[expense.id] = expense

    def remove_expense(self, expense_id):
        self.expenses.pop(expense_id)

    def get_expense_by_id(self,expense_id):
        return self.expenses.get(expense_id)

    def get_expense_by_title(self,expense_title):
        for expense in self.expenses.values():
            if expense.title == expense_title:
                return expense
        return None

    def to_dict(self):
        return {expense_id: expense.to_dict() for expense_id, expense in self.expenses.items()} 


