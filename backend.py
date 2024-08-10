import json

class Expense:
    cats = ('Food', 'Date', 'Misc')

    def __init__(self, cat, price) -> None:
        self.cat = cat
        self.price = price

    def get(self):
        return (self.cat, self.price)
    
class ExpensesList:
    def __init__(self) -> None:
        db = open("./database.json", 'r')
        self.list: dict = json.load(db)
        self.cats = ('Food', 'Date', 'Misc')
        # self.list = {cat:[] for cat in Expense.cats}

    def add_expense(self, cat, price):
        # new_expense = Expense(cat, price)
        if cat in self.cats:
            try:
                self.list[cat].append(price)
            except KeyError:
                self.list[cat] = []
                self.list[cat].append(price)
        else:
            raise ValueError("Category not found.")

    def get_sum_per_cat(self, cat):
        if cat not in self.cats:
            raise ValueError("Category not found.")
        report = sum(self.list[cat])
        return report
    
    # def get_sum_per_cat(self):
    #     report = {cat:sum(self.list[cat]) for cat in self.list.keys()}
    #     return report
    