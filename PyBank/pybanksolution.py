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

#convert Revenue list into int using comprehension
Revnums = [int(revenue) for revenue in Revenue]

#total number of Months
Months = len(Date)
print(Months)
#total Revenue
Revsum = sum(Revnums)
print(Revsum)
#average Revenue
Revavg = Revsum / len(Revnums)
print(Revavg)
#max in Revenue
Revmax = max(Revnums)
print(Revmax)
#min in Revenue
Revmin = min(Revnums)
print(Revmin)
