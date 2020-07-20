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
    print("-" * 50)
    # Read each row of data after the header
    month_count = 0
    Total_profit_loss = 0
    # Profits is a new list holding JUST profit and loss number
    Profits = []
    #Months is a new list JUST for the dates
    Months = []
    # For loop to find total number of months and total amount fo profit/losses
    for row in csvreader:
        month_count = month_count +1
        Total_profit_loss = int(row[1]) + Total_profit_loss
        Profit = row[1]
        Month = row[0]
        Profits.append(Profit)
        Months.append(Month) 

        
    print(f"Total Months:  {month_count}")
    print(f"Total: {Total_profit_loss}")
    average_change = Total_profit_loss/month_count
    print(f"Average Change: {average_change}")
    
    #loop through Profits to find the max and min and then match to corresponding date in Months list
    greatest_increase = int(Profits[0])
    greatest_decrease = int(Profits[0])
    for i in range(0, len(Profits), 1):
        if greatest_increase < int(Profits[i]):
            greatest_increase = int(Profits[i])
            gi_months = Months[i] 
        elif greatest_decrease > int(Profits[i]):
            greatest_decrease = int(Profits[i]) 
            gd_months = Months[i]  
    print(f"Greatest Increase in Profits: {gi_months}  (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {gd_months}  (${greatest_decrease})")
    
 
