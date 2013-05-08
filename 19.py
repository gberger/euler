monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
weekdays = [0, 1, 2, 3, 4, 5, 6]
years = range(1901,2001)
leap = [year for year in range(1901,2001) if year%4==0 and year%400!=0]

currday = 1
currmonth = 1
curryear = 1901
currweek = 2
amt = 0
while curryear<2001:
    if currday == 1 and currweek == 0:
        amt += 1
    currday += 1
    currweek += 1
    if currweek > 6:
        currweek = 0
    if currday > monthdays[currmonth-1]:
        currday = 1
        currmonth += 1
    if currmonth > 12:
        currmonth = 1
        curryear += 1
print amt