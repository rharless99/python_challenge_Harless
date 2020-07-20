import os
import csv


electionpath = os.path.join('Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module

with open(electionpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print("ELECTION RESULTS")
    print("-" * 50)
    total_votes = 0
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_votes = total_votes + 1
    print(f"Total Votes: {total_votes}")
    print("-" * 50)
