import os
#from pathlib import Path
import csv


electionpath = os.path.join('Resources', 'election_data.csv')
output_text_path = os.path.join("Analysis", "PyPollAnalysis.txt")

with open(electionpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    total_votes = 0
    Candidates = []
    Khan_Votes = 0
    Correy_Votes = 0
    Li_Votes = 0
    O_Tooley_Votes = 0

    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
       
        if row[2] == "Khan":
            Khan_Votes = Khan_Votes +1
        elif row[2] == "Correy":
            Correy_Votes = Correy_Votes +1
        elif row[2] == "Li":
            Li_Votes = Li_Votes +1
        elif row[2] == "O'Tooley":
            O_Tooley_Votes = O_Tooley_Votes +1

    if Khan_Votes > Correy_Votes and Khan_Votes > Li_Votes and Khan_Votes > O_Tooley_Votes:
        Winner = "Khan"  
    elif Correy_Votes > Khan_Votes and Correy_Votes > Li_Votes and Correy_Votes > O_Tooley_Votes:
        Winner = "Correy"
    elif Li_Votes > Khan_Votes and Li_Votes > Correy_Votes and Li_Votes > O_Tooley_Votes:
        Winner = "Li"
    elif O_Tooley_Votes > Khan_Votes and O_Tooley_Votes > Correy_Votes and O_Tooley_Votes > Li_Votes:
        Winner = "O'Tooley"

  
    Khan_Percent = Khan_Votes/total_votes
    Khan_Percent = '{0:.3f}'.format(Khan_Percent * 100)        
    Correy_Percent = Correy_Votes/total_votes
    Correy_Percent = '{0:.3f}'.format(Correy_Percent * 100)
    Li_Percent = Li_Votes/total_votes
    Li_Percent = '{0:.3f}'.format(Li_Percent * 100)
    O_Tooley_Percent = O_Tooley_Votes/total_votes
    O_Tooley_Percent = '{0:.3f}'.format(O_Tooley_Percent * 100)
    
   # PyPollAnalysis = (Saveto/"PyPollAnalysis.txt")
    
    #with open(PyPollAnalysis, "w") as txt_file:

    print(f"ELECTION RESULTS")
    print(f"-" * 50)
    print(f"Total Votes: {total_votes}")
    print(f"-" * 50)
    print(f"Khan: {Khan_Percent}%  ({Khan_Votes})")
    print(f"Correy: {Correy_Percent}%  ({Correy_Votes})")
    print(f"Li: {Li_Percent}%  ({Li_Votes})")
    print(f"O'Tooley: {O_Tooley_Percent}%   ({O_Tooley_Votes})")
    print(f"-" * 50)
    print(f"Winner: {Winner}")
    print(f"-" * 50)
    
   
           
    with open(output_text_path, "w") as txt_file:
        L = [f"ELECTION RESULTS\n",
        f"-------------------\n",
        f"Total Votes: {total_votes}\n", 
        f"-------------------\n", 
        f"Khan: {Khan_Percent}%  ({Khan_Votes})\n",
        f"Correy: {Correy_Percent}%  ({Correy_Votes})\n",
        f"Li: {Li_Percent}%  ({Li_Votes})\n",
        f"O'Tooley: {O_Tooley_Percent}%   ({O_Tooley_Votes})\n",
        f"-------------------\n",
        f"Winner: {Winner}\n",
        f"-------------------\n"
        ]
        txt_file.writelines(L)         
        txt_file.close() 
        
        
        
        
        
        
      

    






 
