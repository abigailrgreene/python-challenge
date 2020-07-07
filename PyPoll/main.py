# Import OS
import os

# Import CSV reader module
import csv 



csvpath = os.path.join ('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    

    print(csvreader)

    num_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in csvreader:
        if row[2] == "Candidate":
            continue 
        num_votes += 1
        if row[2] == "Khan":
            khan_votes += 1
        if row[2] == "Correy":
            correy_votes += 1
        if row[2] =="Li":
            li_votes += 1
        if row[2] =="O'Tooley":
            otooley_votes +=1
    

    results_str = ""

    results_str = results_str + "-----------------------------------------" + "\n"

    results_str = results_str + "Election Results" + "\n"

    results_str = results_str + "-----------------------------------------" + "\n"
 
    results_str = results_str + f"Total Votes: {num_votes}" + "\n"

    results_str = results_str + "-----------------------------------------" + "\n"

    results_str = results_str + f"Khan: {round((khan_votes/num_votes)*100)}% ({khan_votes})" + "\n"
  
    results_str = results_str + f"Correy: {round((correy_votes/num_votes)*100)}% ({correy_votes})" + "\n"
   
    results_str = results_str + f"Li: {round((li_votes/num_votes)*100)}% ({li_votes})" + "\n"

    results_str = results_str + f"O'Tooley: {round((otooley_votes/num_votes)*100)}% ({otooley_votes})" + "\n"

    results_str = results_str + "-----------------------------------------" + "\n"

    if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
        results_str = results_str + "Winner: Khan" + "\n"
    if correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
        results_str = results_str + "Winner: Correy" + "\n"
    if li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
        results_str = results_str + "Winner: Li" + "\n"
    if otooley_votes > khan_votes and otooley_votes > li_votes and otooley_votes > correy_votes:
        results_str = results_str + "Winner: O'Tooley" + "\n"


print(results_str)

analysis_filepath = os.path.join("Analysis","Analysis.txt")

text_file = open(analysis_filepath,"w")
text_file.write(results_str)
text_file.close