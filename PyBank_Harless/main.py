import os
import csv


budgetpath = os.path.join('Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

with open(budgetpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print("FINANCIAL ANALYSIS")
    print("_" * 50)
    # Read each row of data after the header
    month_count = 0
    Total_profit_loss = 0
    # For loop tofind total number of months and total amount fo profit/losses
    for row in csvreader:
        month_count = month_count +1
        Total_profit_loss = int(row[1]) + Total_profit_loss
    print(f"Total Months:  {month_count}")
    print(f"Total: {Total_profit_loss}")
    average_change = Total_profit_loss/month_count
    print(f"Average Change: {average_change}")
