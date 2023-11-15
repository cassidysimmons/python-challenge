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

# return to the first row...
    csvfile.seek(0)
    next(csvreader)

    for col in csvreader:
        for col[2] == "Charles Casper Stockham":
            casper = len(col[2])
        
    print(casper)
