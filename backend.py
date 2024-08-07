class Expense:
    ITEMS = ('Food', 'Date', 'Misc')

    def __init__(self, item, price) -> None:
        self.item = item
        self.price = price

    def get(self):
        return (self.item, self.price)
    
class ExpensesList:
    def __init__(self) -> None:
        self.list = {item:[] for item in Expense.ITEMS}

    def add_expense(self, item, price):
        new_expense = Expense(item, price)
        self.list[item].append(price)

    def get_expenses(self):
        report = {item:sum(self.list[item]) for item in self.list.keys()}
        return report
    