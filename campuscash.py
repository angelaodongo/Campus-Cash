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

    1. View total spending
    2. View remaining budget
    3. Exit
    """)

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            expense = int(input("Enter your expense amount: "))
            total_spend = total_spend + expense
            print(f"Your total spend is: {total_spend}")
        case 2:
            expense = int(input("Enter your expense amount: "))
            remaining = b - expense
            print(f"Your remaining budget is: {remaining}")
        case 3:
            print("Goodbye!")
        case _:
            print("Invalid input. Please try again.")

main()