# Expense Tracker Projects

expenseList = []  # List of all expenses in form of dictionary

print("Welcome to Expense Tracker : ")

while True:
    print("\n==== Menu ====")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View total Expense")
    print("4. Exit")

    choice = int(input("Please Enter your choice: "))

    # Add expense
    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter the category (food , travel , books): ")
        description = input("Enter short Description: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseList.append(expense)
        print("\nThe expense is added successfully")

    # View all expenses
    elif choice == 2:
        if len(expenseList) == 0:
            print("No Expense Added")
        else:
            print("==== This is your all Expense ====")
            count = 1
            for item in expenseList:
                print(f"{count} -> {item['date']} , {item['category']} , {item['description']} , {item['amount']}")
                count += 1

    # View Total spending
    elif choice == 3:
        total = 0
        for item in expenseList:
            total += item["amount"]

        print("\nTotal Expense:", total)

    # EXIT
    elif choice == 4:
        print("Thanks for using the Expense Tracker")
        break

    else:
        print("Invalid Choice.. Try Again....")