import csv

#define where CSV is
datapath = "raw_data/budget_data_2.csv"

#storing contents of columns A and B
Date = []
Revenue = []

#open CSV to read
with open(datapath, newline='') as budgetdata:

    budgetreader = csv.reader(budgetdata, delimiter=',')

    next(budgetreader)

    for column in budgetreader:
        Date.append(column[0])
        Revenue.append(column[1])

#convert Revenue list into int using enumerate
Revnums = [int(revenue) for revenue in Revenue]

# #total number of Months
Months = len(Date)
# #total Revenue
Revsum = sum(Revnums)
# #average Revenue
Revavg = Revsum / len(Revnums)
# #determine max Revenue with Month
Revmax = max(Revnums)
# #determine min Revenue with Month
Revmin = min(Revnums)

# #print to terminal
print("`" * 3)
print("Financial Analysis")
print("-" * 28)
print(f"Total Months: {Months}")
print(f"Total Revenue: ${Revsum}")
print(f"Average Revenue Change: ${Revavg}")
print(f"Greatest Increase in Revenue: (${Revmax})")
print(f"Greatest Decrease in Revenue: (${Revmin})")
print("`" * 3)
