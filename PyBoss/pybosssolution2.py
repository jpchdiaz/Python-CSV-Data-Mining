import csv

#define where csv is
datapath = "raw_data/employee_data1.csv"

new_employee_list = []

with open(datapath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lastssn = row["SSN"].split('-')[2]
        newssn = f"***-**-{lastssn}"
        print(newssn)
