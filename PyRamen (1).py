# -*- coding: UTF-8 -*-
"""
PyRamen Homework Starter.

Author: Tracy I. Ejiogu
Date: June 27, 2023

"""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    menu = list(csvreader)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    sales = list(csvreader)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sale in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(sale[3])
    menu_item = sale[4]

    # @TODO: If the item value not in the report, add it as a new entry with initialized metrics
    if menu_item not in report:
        report[menu_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for item in menu:
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item_name = item[0]
        price = float(item[3])
        cost = float(item[4])

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to any of the items in the menu, then begin tracking metrics for that item
        if menu_item == item_name:
            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity

    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(f"Total number of records in sales data: {row_count}")

# @TODO: Write out report to a text file (won't appear on the command line output)
with open('pyramen_report.txt', 'w') as file:
    for item, metrics in report.items():
        file.write(f"{item}{metrics}\n")