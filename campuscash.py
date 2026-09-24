def main():
    print(""" 
    ============================================
                    CAMPUSCASH
                Student Budget Planner
    ============================================
    """)
    budget = int(input("Enter your budget: "))
    menu(budget)

def menu(b):
    print(f"Your budget is: {b}")
    print(""" 
    What would you like to do?

    1. Add an expense
    2. View total spending
    3. View remaining budget
    4. Exit
    """)

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            expense = int(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            print(expense, description)
        case 2:
            expense = int(input("Enter your expense amount: "))
            total_spend = total_spend + expense
            print(f"Your total spend is: {total_spend}")
        case 3:
            expense = int(input("Enter your expense amount: "))
            total_spend = total_spend + expense
            remaining = b - total_spend
            print(f"Your remaining budget is: {remaining}")
        case 4:
            print("Goodbye!")
        case _:
            print("Invalid input. Please try again.")

main()