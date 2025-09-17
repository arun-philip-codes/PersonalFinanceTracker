import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.rubber_prices = []
    
    def add_expense(self, amount, category, description):
        expense = {
            'date': datetime.now().isoformat(),
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        print(f"Added expense: {description} - ₹{amount}")
    
    def track_rubber_price(self, price_per_kg):
        price_entry = {
            'date': datetime.now().isoformat(),
            'price_per_kg': price_per_kg,
            'location': 'Kanjirappally Market'
        }
        self.rubber_prices.append(price_entry)
    
    def monthly_summary(self):
        total = sum(exp['amount'] for exp in self.expenses)
        return f"Monthly expenses: ₹{total}"
