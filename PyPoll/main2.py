import csv

#define where csv is
datapath = "raw_data/election_data_2.csv"

#store contents of columns
id = []
county = []
candidate = []

#open CSV to read
with open(datapath, newline='') as votedata:

    votereader = csv.reader(votedata, delimiter=',')

    next(votereader)

    for column in votereader:
        id.append(column[0])
        county.append(column[1])
        candidate.append(column[2])

#votes cast
totalvotes = len(candidate)
#candidate list
names = list(set(candidate))
#winner
winner = max(set(candidate), key=candidate.count)

print("```")
print("Election Results")
print("-------------------------")
#Total number of votes cast
print(f'Total Votes: {totalvotes}')
print("-------------------------")
for i in range(len(names)):
    cannames = names[i]
    perc = (candidate.count(names[i]) * 100) / totalvotes
    votesper = candidate.count(names[i])
    print(f"{cannames}: {perc}% ({votesper})")
print("-------------------------")
#Winner of the election
print(f"Winner: {winner}")
print("-------------------------")
print("```")

#Write to text file
with open("results_2.txt", 'w') as textfile:
    print("```", file=textfile)
    print("Election Results", file=textfile)
    print("-------------------------", file=textfile)
    print(f'Total Votes: {totalvotes}', file=textfile)
    print("-------------------------", file=textfile)
    for i in range(len(names)):
        cannames = names[i]
        perc = (candidate.count(names[i]) * 100) / totalvotes
        votesper = candidate.count(names[i])
        print(f"{cannames}: {perc}% ({votesper})", file=textfile)
    print("-------------------------", file=textfile)
    print(f"Winner: {winner}", file=textfile)
    print("-------------------------", file=textfile)
    print("```", file=textfile)
