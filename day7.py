# Day 7 Challenge:
# The city’s bus system carries 1,200,000 people each day.
# How many people does the bus system carry each year? (1 year = 365 days)
# Solve without using *,/operator, bitwise operator or loop.

def multiply(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + multiply(x, y - 1)
    if y < 0:
        return -multiply(x, -y)


perday = 1200000
peryear = 365
peopleperyear = multiply(perday, peryear)

print(peopleperyear)
