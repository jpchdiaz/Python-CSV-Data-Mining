import csv

#define where csv is
datapath = "raw_data/employee_data2.csv"

new_employee_list = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

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
        lastssn = row["SSN"].split('-')[2]
        newssn = f"***-**-{lastssn}"
        #State -- thanks, dictionaries.py from session 3!
        state = row["State"]
        abbrev = f"{us_state_abbrev[state]}"
        new_employee_list.append(
            {   "Emp ID": row["Emp ID"],
                "First Name": row["Name"].split()[0],
                "Last Name": row["Name"].split()[1],
                "DOB": newdate,
                "SSN": newssn,
                "State": abbrev
            }
        )

newpath = 'newemployees_2.csv'
with open(newpath, "w", newline='') as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_list)
