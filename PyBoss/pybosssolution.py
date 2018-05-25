import csv
import datetime

#define where csv is
datapath = "raw_data/employee_data1.csv"

new_employee_list = []

#censors first 5 numbers of SSN. ugliest code i've written to date.
def censor(ssnkey):
    asterisks = "***-**"
    for i in range(len(ssnkey)):
        words = list(ssnkey[i])
        del(words[0])
        del(words[0])
        del(words[0])
        del(words[0])
        del(words[0])
        del(words[0])
        ssnkey[i] = "".join(words)
        ssnkey[i] = asterisks + ssnkey[i]

with open(datapath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Name
        first = row["Name"].split()[0]
        last = row["Name"].split()[1]
        #DOB
        year = row["DOB"].split("-")[0]
        month = row["DOB"].split("-")[1]
        day = row["DOB"].split("-")[2]
        newdate = f"{month}/{day}/{year}"
        #SSN

        #State
        state = row["State"]
        new_employee_list.append(
            {   "Emp ID": row["Emp ID"],
                "First Name": row["Name"].split()[0],
                "Last Name": row["Name"].split()[1],
                "DOB": newdate,
                "SSN": newssn,
                "State": "State"
            }
        )

newpath = 'newemployees.csv'
with open(newpath, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)
