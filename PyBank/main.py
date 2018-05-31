import csv

#define where CSV is
datapath = "raw_data/budget_data_1.csv"

#storing contents of columns A and B
Date = []
Revenue = []

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
revenue_changes = []

#open CSV to read
with open(datapath, newline='') as budgetdata:

    budgetreader = csv.reader(budgetdata, delimiter=',')

    next(budgetreader)

    for column in budgetreader:
        Date.append(column[0])
        Revenue.append(column[1])

        #increase/decrease calculations
        revenue_change = int(column[1]) - prev_revenue

        #resets value of prev_revenue to row where analysis completed
        prev_revenue = int(column[1])

        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = column[0]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = column[0]

        revenue_changes.append(int(column[1]))

#convert Revenue list into int using enumerate
Revnums = [int(revenue) for revenue in Revenue]

# total number of Months
Months = len(Date)
# total Revenue
Revsum = sum(Revnums)
# average Revenue
Revavg = round(Revsum / len(Revnums), 2)

# #print to terminal
print("`" * 3)
print("Financial Analysis for budget_data_1.txt")
print("-" * 28)
print(f"Total Months: {Months}")
print(f"Total Revenue: ${Revsum}")
print(f"Average Revenue Change: ${Revavg}")
print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})")
print("`" * 3)
print(" ")
print("Exporting as analysis1.txt...")

#print to file
with open("analysis1.txt", 'w') as textfile:
    print("`" * 3, file=textfile)
    print("Financial Analysis", file=textfile)
    print("-" * 28, file=textfile)
    print(f"Total Months: {Months}", file=textfile)
    print(f"Total Revenue: ${Revsum}", file=textfile)
    print(f"Average Revenue Change: ${Revavg}", file=textfile)
    print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})", file=textfile)
    print(f"Greatest Increase in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})", file=textfile)
    print("`" * 3, file=textfile)
