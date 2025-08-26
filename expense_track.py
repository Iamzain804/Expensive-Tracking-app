from Main import Expense
import calendar
import datetime

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expense.csv"
    budget = 150000

    # Get user input for expense
    expense = Get_user_input()

    # Write expense to file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expenses(expense_file_path, budget)


def Get_user_input():
    print(f"Running Expense Tracker!")
    expense_name = input("Enter expense name: ")
    expense_amount = int(input("Enter expense amount: "))

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎯 Fun",
        "🚗 Wheels_Tuning"
    ]

    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_categories, start=1):
            print(f" {i}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name,
                category=selected_category,
                amount=expense_amount
            )
            print(new_expense)
            return new_expense
        else:
            print("Invalid category. Please try again.")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name.strip()},{expense.amount},{expense.category.strip()}\n")


def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing User Expense")
    expenses: list[Expense] = []

    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            parts = [part.strip() for part in line.strip().split(",")]
            if len(parts) != 3:
                continue  # Skip bad lines
            expense_name, expense_amount, expense_category = parts
            try:
                line_expense = Expense(
                    name=expense_name,
                    amount=int(expense_amount),
                    category=expense_category
                )
                expenses.append(line_expense)
            except ValueError:
                continue  # Skip lines with bad amount

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.amount

    print("Expenses By Category 📈")
    for key, amount in amount_by_category.items():
        print(f"{key}: PKR {amount}")

    total_spent = sum(ex.amount for ex in expenses)
    print(f"🧾 Total Spent: PKR {total_spent} this month! ")

    remaining_budget = budget - total_spent
    print(f"🧮 Budget Remaining: PKR {remaining_budget} this month! ")

    today = datetime.date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]
    remaining_days = last_day - today.day

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(green(f"Budget Per Day: PKR {daily_budget}"))
    else:
        print("No days remaining in this month.")


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
