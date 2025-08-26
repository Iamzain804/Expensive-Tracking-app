# Expense Tracker

## Overview
Expense Tracker is a command-line Python application designed to help users manage their personal expenses. It allows users to log expenses with names, amounts, and categories, save them to a CSV file, and summarize spending by category while tracking against a monthly budget. The application provides insights into total spending, remaining budget, and daily budget for the rest of the month.

Built with Python, this project is lightweight, easy to use, and ideal for personal finance tracking.

## Features
- **Log Expenses**: Input expense details (name, amount, and category) via a user-friendly command-line interface.
- **Categorize Spending**: Choose from predefined categories like Food, Home, Work, Fun, and Wheels Tuning.
- **Save to CSV**: Expenses are stored in a CSV file (`expense.csv`) for persistence.
- **Summarize Expenses**: View expenses by category, total spent, remaining budget, and daily budget for the current month.
- **Colorful Output**: Budget per day is displayed in green for better visibility.

## Prerequisites
- Python 3.6 or higher
- No external libraries are required (uses standard Python libraries like `calendar` and `datetime`).

## Installation
Follow these steps to set up the Expense Tracker on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. **Ensure Python is installed**:
   Verify Python installation by running:
   ```bash
   python --version
   ```
   If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

3. **Set up the project**:
   The project includes an example `expense.csv` file. If it doesn't exist, it will be created automatically when you log an expense.

## Usage
1. Run the application:
   ```bash
   python expense_track.py
   ```

2. Follow the prompts:
   - Enter the expense name (e.g., "Laptop").
   - Enter the expense amount (e.g., `8900`).
   - Select a category by entering a number from the list (e.g., `1` for 🍔 Food, `2` for 🏠 Home, etc.).

3. View the summary:
   - The application will display expenses by category, total spent, remaining budget, and daily budget for the current month.

Example output:
```
Running Expense Tracker!
Enter expense name: Laptop
Enter expense amount: 8900
Select a category:
 1. 🍔 Food
 2. 🏠 Home
 3. 💼 Work
 4. 🎯 Fun
 5. 🚗 Wheels_Tuning
Enter a category number [1 - 5]: 2
<Expense:Laptop , 🏠 Home ,PKR8900 >
🎯 Saving User Expense: <Expense:Laptop , 🏠 Home ,PKR8900 > to expense.csv
Summarizing User Expense
Expenses By Category 📈
🏠 Home: PKR 8900
🧾 Total Spent: PKR 8900 this month!
🧮 Budget Remaining: PKR 141100 this month!
Budget Per Day: PKR 7055.0
```

## Project Structure
```
expense-tracker/
├── expense_track.py    # Main script for expense tracking logic
├── Main.py            # Defines the Expense class
├── expense.csv        # Stores expense data
└── README.md          # This file
```

## Notes
- The default monthly budget is set to PKR 150,000 in `expense_track.py`. You can modify the `budget` variable in the code to change this.
- The application assumes the `expense.csv` file is in the project root. Ensure it has write permissions.
- Invalid inputs (e.g., non-numeric amounts or invalid categories) are handled gracefully with prompts to retry or skip.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

Please include tests for new features and follow Python PEP 8 style guidelines.

## License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

## Contact
For questions or feedback, reach out to [your-username] at [your-email@example.com] or open an issue on GitHub.