"""
PyBank python-challenge.

Author: Tracy I. Ejiogu
Date: June 27, 2023

"""

# Import required libraries
import csv
import os

# File path
file_path = os.path.join("budget_data.csv")

# Initialize variables
total_months = 0
net_profit_loss = 0
previous_month_profit_loss = None
change_profit_loss = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]

# Open the file
try:
    with open(file_path, "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)

        # Loop through each row in the file
        for row in csvreader:
            try:
                # Increment total_months and add to net_profit_loss
                total_months += 1
                net_profit_loss += int(row[1])

                # Calculate change in profit/loss, if not in first row
                if previous_month_profit_loss is not None:
                    change = int(row[1]) - previous_month_profit_loss
                    change_profit_loss.append(change)

                    # Is the change a new greatest_increase or greatest_decrease?
                    if change > greatest_increase[1]:
                        greatest_increase = [row[0], change]
                    if change < greatest_decrease[1]:
                        greatest_decrease = [row[0], change]

                # Set profit/loss for next row's comparison
                previous_month_profit_loss = int(row[1])
            except ValueError as e:
                # Print error message if row contains invalid data
                print(f"Row {total_months + 1} has invalid data: {e}")
except FileNotFoundError:
    # Print error message if file is not found
    print(f"{file_path} does not exist.")

# Calculate average change
average_change = round(sum(change_profit_loss) / len(change_profit_loss), 2)

# Print analysis
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit_loss}\n"
    f"Average  Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output)

# Write analysis to a text file
with open("financial_analysis.txt", "w") as txt_file:
    txt_file.write(output)