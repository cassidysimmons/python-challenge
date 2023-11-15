# 1. make a loop to count all the rows in cloumn one
# 2. (net total) add all the profits/ losses from column two
# 3. average change of profits/ losses
# 4. greatest increase + date
# 5. greatest decrease + date

import csv
import os

csvpath = os.path.join("..", "pyBank", "resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print("financial analysis")
    print("----------------------------------------")

# print the number of months (rows) in the file
    months = (len(list(csvreader)))
    print("total months:" , months)

# start back at row one...
    csvfile.seek(0)
    next(csvreader)

    # sets the beginning total value to zero
    total = 0

    for col in csvreader:

        total += int(col[1])
    print("total: $" , total)
# ============================================================

# start back to row 1...
    csvfile.seek(0)

# !! creates a list of the rows in the file !!
    listofrows = list(csvreader)

# pulls the 2* row from the list we created, with an index of 1 (2nd value*)
    firstrow = listofrows[1][1]
    lastrow = listofrows[86][1]

    change = int(lastrow) - int(firstrow)
    print("average change: $" , round(change / 85, 2))
# ==============================================================

    csvfile.seek(0)
    next(csvreader)

    netlist = []
    firstrow = next(csvreader)
    prevnet = int(firstrow[1])

    for col in csvreader:
        change = int(col[1]) - prevnet
        netlist += [change]
        increase = max(netlist)
        decrease = min(netlist)

    averagechange = sum(netlist) / len(netlist)
    print(averagechange)


# =============================================================

    print("greatest increase in profits:", increase)
    print("greatest decrease in profits:", decrease)


