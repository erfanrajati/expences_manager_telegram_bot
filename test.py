from backend import *

newList = ExpensesList()


newList.add_expense("Misc", 320)
newList.add_expense("Date", 200)
newList.add_expense("Food", 200)
newList.add_expense("Food", 200)
newList.add_expense("Date", 100)
newList.add_expense("Food", 100)
newList.add_expense("Misc", 100)
newList.add_expense("Food", 150)
newList.add_expense("Date", 150)
newList.add_expense("Food", 150)
newList.add_expense("Misc", 150)

misc = newList.get_sum_per_cat("Misc")
food = newList.get_sum_per_cat("Food")
date = newList.get_sum_per_cat("Date")

print(misc, food, date)