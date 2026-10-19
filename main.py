
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

    expense = {"amount": amount, "category": category}
    expenses.append(expense)

    print("Expense added SUCCESSFULLY.")





def main():
    expenses = []
    while True:
        show_menu()
        choice = input("choose an Option: ") # the input always return a string, so vhoice variable is string also

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