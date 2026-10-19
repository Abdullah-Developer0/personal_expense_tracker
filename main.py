
def show_menu():
    print("\n=== Expense tracker ===") # \n adds a blank line before the title for readability.
    print("1. add a new expense")
    print("2. show all expenses")
    print("3. Exit")
    # here we did not write any return becuase the function only prints, nothing coming back.

def main():
    expenses = []
    while True:
        show_menu()
        choice = input("choose an Option: ") # the input always return a string, so vhoice variable is string also

        if choice == "1":
            print("")
        if choice == "2":
            print("")
        if choice == "3":
            break
        else:
            print("Invalid Choice, please try again.")

if __name__ == "__main__":
    main()