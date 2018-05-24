import csv
import datetime

#define where csv is
datapath = "raw_data/employee_data1.csv"

new_employee_list = []

with open(datapath) as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader)
    for row in reader:
        #DOB
        month = row[2].split("/")[0]
        day = row[2].split("/")[1]
        year = row[2].split("/")[2]
        #SSN
        SSN = row[3]

        new_employee_list.append(
            {   "Emp ID": row["Emp ID"]
                "First Name": row[1].split()[0]
                "Last Name": row[1].split()[1]
                "DOB": year + "-" + month + "-" + day
                "SSN":
                "State"
            }
        )

newpath = 'newemployees.csv'
with open(newpath, "w") as csvfile:
