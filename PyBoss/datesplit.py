dates = ["12/4/1985", "9/8/1993", "12/20/1957"]

month =[i.split("/")[0] for i in dates]
day = [i.split("/")[1] for i in dates]
year = [i.split("/")[2] for i in dates]

newdates = zip(year, month, day)

print(dates)
print(list(newdates))
