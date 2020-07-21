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
    Candidates = []
    Khan_Votes = 0
    Correy_Votes = 0
    Li_Votes = 0
    O_Tooley_Votes = 0

    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        #Candidate = row[2]
        #Candidates.append(Candidate)
        if row[2] == "Khan":
            #print(row)
            Khan_Votes = Khan_Votes +1
        elif row[2] == "Correy":
            Correy_Votes = Correy_Votes +1
        elif row[2] == "Li":
            Li_Votes = Li_Votes +1
        elif row[2] == "O'Tooley":
            O_Tooley_Votes = O_Tooley_Votes +1

            

    #print(Candidates) 

   


    # for can in range(0, len(Candidates), 1):
    #     if can == "Khan":
    #         Khan_Votes = Khan_Votes + 1
    #     elif can == "Correy":
    #         Correy_Votes = Correy_Votes+1
    #     elif can == "Li":
    #         Li_Votes = Li_Votes +1
    #     elif can == "O'Tooley":
    #         O_Tooley_Votes = O_Tooley_Votes +1

       
    Khan_Percent = Khan_Votes/total_votes
    Khan_Percent = round(Khan_Percent, 5)* 100        
    Correy_Percent = Correy_Votes/total_votes
    Correy_Percent = round(Correy_Percent, 5) * 100
    Li_Percent = Li_Votes/total_votes
    Li_Percent = round(Li_Percent, 2) * 100
    O_Tooley_Percent = O_Tooley_Votes/total_votes
    O_Tooley_Percent = round(O_Tooley_Percent, 5)* 100
    
    print(f"Total Votes: {total_votes}")
    print("-" * 50)
    print(f"Khan: {Khan_Percent}%  ({Khan_Votes})")
    print(f"Correy: {Correy_Percent}%  ({Correy_Votes})")
    print(f"Li: {Li_Percent}%  ({Li_Votes})")
    print(f"O'Tooley: {O_Tooley_Percent}%   ({O_Tooley_Votes})")
    print("-" * 50)
    print(f"Winner: Khan")

    print("-" * 50)




 
