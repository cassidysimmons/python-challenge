# modules
import os
import csv

csvpath = os.path.join("..", "pyPoll", "resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print("election results")
    print("---------------------------------")

# print number of votes (rows) in the file
    rows =list(csvreader)
    votes = len(rows)
    print("total votes:", votes)
    print("---------------------------------")

#=================================================================
# return to the first row...
    csvfile.seek(0)
    next(csvreader)

    casperlist = []
    row = next(csvreader)

    for col in csvreader:
        if col[2] == "Charles Casper Stockham":
            
            casperlist += [row]

    print("Charles Casper Stockham:", 
           round(((len(casperlist)/ votes) *100), 3) , "%" ,
    "(" , len(casperlist) , ")" )
# ===============================================================
# return to the first row...
    csvfile.seek(0)
    next(csvreader)

    dianalist = []
    row = next(csvreader)

    for col in csvreader:
        if col[2] == "Diana DeGette":
            
            dianalist += [row]

    print("Diana DeGette:", 
           round(((len(dianalist)/ votes) *100), 3) , "%" ,
    "(" , len(dianalist) , ")" )
# ===============================================================
# return to the first row...
    csvfile.seek(0)
    next(csvreader)

    raylist = []
    row = next(csvreader)

    for col in csvreader:
        if col[2] == "Raymon Anthony Doane":
            
            raylist += [row]

    print("Raymon Anthony Doane:", 
           round(((len(raylist)/ votes) *100), 3) , "%" ,
    "(" , len(raylist) , ")" )
# ===============================================================

    print("---------------------------------")

# since the percentages are already calculated, we can just look and manually print the winner
    print("winner: Diana Degette")
    
    print("---------------------------------")
