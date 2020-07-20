import os
import csv




budgetpath = os.path.join('Resources', 'budget_data.csv')
#analysispath = os.path.join('Analysis', 'BudgetAnalysis.txt')

#Read using CSV module

with open(budgetpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
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
        Profit = int(row[1])
        Month = row[0]
        
        Profits.append(Profit)
        Months.append(Month) 

        
    print(f"Total Months:  {month_count}")
    print(f"Total: {Total_profit_loss}")
  
    
    #loop through profits and find the difference and store those differences in a new list called PL_changes
    PL_changes = []
    for i in range(1, len(Profits)):
        PL_changes.append(Profits[i] - Profits[i-1])
    
    #Loop through PL_changes list and find the total
    Total_Changes = PL_changes[0]
    for i in range(1, len(PL_changes)): 
        Total_Changes = Total_Changes + PL_changes[i] 
    
    #print(Total_Changes)
    Average = Total_Changes/len(PL_changes)
    Average = round(Average, 2)
    print(f"Average Change: ${Average}")

    #Loop through PL_changes to find the greatest increase and the greatest decrease
    greatest_increase = PL_changes[0]
    greatest_decrease = PL_changes[0]
    for a in range(0, len(PL_changes), 1):
        if greatest_increase < PL_changes[a]:
            greatest_increase = PL_changes[a]
            gi_months = Months[a+1]
        elif greatest_decrease > PL_changes[a]:
            greatest_decrease = PL_changes[a]
            gd_months = Months[a+1]
    print(f"Greatest Increase in Profits: {gi_months} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {gd_months} (${greatest_decrease})")


  
    
    

   
