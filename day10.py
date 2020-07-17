# Day 10 Challenge:
# Salesperson Rita drives 2,052 miles in 6 days, stopping at 2 towns each day. How many kilometres
# does she average between stops?

totalmiles = 2052
days = 6
stopsperday = 2
totalstops = days * stopsperday
avgperstop = totalmiles / totalstops

inkm = avgperstop * 1.6

print(f"{inkm} KM")
