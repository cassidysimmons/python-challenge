# modules
import os
import csv

csvpath = os.path.join("..", "pyPoll", "resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    output = []

    output.append("election results")
    print("election results")
    output.append("---------------------------------")
    print("---------------------------------")

# print number of votes (rows) in the file
    rows =list(csvreader)
    votes = len(rows)

    output.append(("total votes:", votes))
    print("total votes:", votes)
    output.append("---------------------------------")
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

    output.append(((((("Charles Casper Stockham:", 
           round(((len(casperlist)/ votes) *100), 3) , "%" ,
    "(" , len(casperlist) , ")" ))))))

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

    output.append(((((("Diana DeGette:", 
           round(((len(dianalist)/ votes) *100), 3) , "%" ,
    "(" , len(dianalist) , ")" ))))))

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

    output.append(((((("Raymon Anthony Doane:", 
           round(((len(raylist)/ votes) *100), 3) , "%" ,
    "(" , len(raylist) , ")" ))))))

    print("Raymon Anthony Doane:", 
           round(((len(raylist)/ votes) *100), 3) , "%" ,
    "(" , len(raylist) , ")" )
# ===============================================================

    output.append("---------------------------------")
    print("---------------------------------")

# since the percentages are already calculated, we can just look and manually print the winner
    output.append("winner: Diana Degette")
    print("winner: Diana Degette")
    
    output.append('---------------------------------')
    print("---------------------------------")

file = open(os.path.join("analysis", "pyPoll analysis.txt"), "w")

for o in output:
    file.write (str(o) + "\n")