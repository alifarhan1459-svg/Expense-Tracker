import csv

FILE_NAME = "expenses.csv"

def add_expense():
    desc = input("Enter expense description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([desc, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} - ₹{row[1]}")
    except FileNotFoundError:
        print("No expenses found.")

def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])

        print("Total Expense =", total)
    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        break
