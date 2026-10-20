
def show_menu():
    print("\n=== Expense tracker ===") # \n adds a blank line before the title for readability.
    print("1. add a new expense")
    print("2. show all expenses")
    print("3. Exit")
    # here we did not write any return becuase the function only prints, nothing coming back.

def add_expense(expenses):
    amount_input = input("Enter The Amount: ")

    # here we use try/except to convert the string value to a number(float)
    try:
        amount = float(amount_input) # as we say input always return str so here we
    except ValueError: # if the string we get from amount_input isn't a number then the converting procees will not be completed
        print("Invalid amount, expense not added")
        return

    if not (0 < amount < float("inf")): # float can be -5 or 0, so here must be check it's a positive number
        print("amount must be a positive number, expense not added")
        return

    category = input("Enter the name of category: ").strip() # strip() it's a function remove any extra spaces

    if category == "": # check the category if it's not empty
        print ("category cannot be wmpty, expense not added")
        return

    expense = {"amount": amount, "category": category} # create a dictonary to store to values under one key
    expenses.append(expense)

    print("Expense added SUCCESSFULLY.")

def show_expenses(expenses):
    if len(expenses) == 0:
        print("no expenses recorded yet.")
        return

    print("\n === All Expenses ===")
    for index, expense in enumerate(expenses, start=1): # enumerate() returns a pair (tuple) for each item:(number, item), starting from zero by default & start=1 makes counting begin at 1 instead of 0.
        print(f"{index}. {expense['category']} - ${expense['amount']}")

def delete_expense(expenses):
    if len(expenses) == 0: # check if the list is empty
        print("No expesnes to delete.")
        return

    show_expenses(expenses)
    choice = input("Enter the number of the expense to delete: ")

    try:
        index = int(choice)
    except ValueError:
        print("Invalid input, please enter a number.")
        return

    if index < 1 or index > len(expenses):
        print("No expense with that number.")
        return

    removed = expenses.pop(index - 1) # number the user sees (starts at 1) and Python's internal index (starts at 0) & pop() is a list method that removed an item
    print(f"Deleted: {removed['category']} - ${removed['amount']}")

def show_summary(expenses):
    if len(expenses) == 0:
        print("No expenses to summarize.")
        return

    amounts = [expense["amount"] for expense in expenses] # storing numbers in a list
    categories = {expense[category] for expense in expenses} # storing the categoris from dict.. to set, set: don't reapet items

    total = sum(amounts)
    highest = max(amounts)
    lowest = min(amounts)

    print("\n=== Summary ===")
    print(f"Total: ${total}")
    print(f"Highest expense: ${highest}")
    print(f"Lowest expense: ${lowest}")
    print(f"Categories used: {', '.join(categories)}")

def main():
    expenses = []
    while True:
        show_menu()
        choice = input("choose an Option: ") # the input always return a string, so choice variable is string also

        if choice == "1":
            add_expense(expenses)
        if choice == "2":
            print("")
        if choice == "3":
            break
        else:
            print("Invalid Choice, please try again.")

if __name__ == "__main__":
    main()