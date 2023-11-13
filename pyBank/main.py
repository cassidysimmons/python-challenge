# 1. make a loop to count all the rows in cloumn one
# 2. (net total) add all the profits/ losses from column two
# 3. average change of profits/ losses
# 4. greatest increase + date
# 5. greatest decrease + date

# modules
import os
import csv

csvpath = os.path.join("..","pyBank","resources","budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# header*
    print("financial analysis")
    print("--------------------------------------------------")

# set beginning value to zero
    total = 0

    for col in csvreader:
# -- only prints row one ??? --
        print(col)

# print the number of months (rows) in the file
        months = (len(list(csvreader)))
        print("total months:" , months + int(1))


# -- not working, only printing row one value ?? --
        total += int(col[1])
        print("total: $" , total)

# -- how do i pull a specific 'cell' value, need last value of col 1 ?? --
        change = int(col[1]) - int(col[1])
        print("average change: $" , change)