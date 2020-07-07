# Import OS
import os

# Import CSV reader module
import csv 



csvpath = os.path.join ('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    

    print(csvreader)

    total = 0
    num_months = 0
    mini = 999999999999999999
    maxi = -999999999999999999
    min_str = ""
    max_str = ""

    for row in csvreader:
        if row[1] == "Profit/Losses":
            continue 
        num_months += 1
        val = int(row[1]) 
        date = row[0]
        total += val
        if val < mini:
            min_str = "Greatest Decrease in Profits: " + date + " (" + row[1] + ")"
            mini = val
        if val > maxi:
            max_str = "Greatest Increase in Profits: " + date + " (" + row[1] + ")"
            maxi = val


    results_str = ""

    print("----------------------")
    results_str = results_str + "-----------------------------------------" + "\n"
    print("Financial Analysis")
    results_str = results_str + "Financial Analysis" + "\n"
    print("----------------------")
    results_str = results_str + "-----------------------------------------" + "\n"
    print(f"Total Months: {num_months}")
    results_str = results_str + f"Total Months: {num_months}" + "\n"
    print(f"Total: ${total}")
    results_str = results_str + f"Total: ${total}" + "\n"
    print(f"Average Change: {total/num_months}")
    results_str = results_str + f"Average Change: {total/num_months}" + "\n"
    print(max_str)
    results_str = results_str + max_str + "\n"
    print(min_str)
    results_str = results_str + min_str + "\n"

analysis_filepath = os.path.join("Analysis","Analysis.txt")

text_file = open(analysis_filepath,"w")
text_file.write(results_str)
text_file.close




        







