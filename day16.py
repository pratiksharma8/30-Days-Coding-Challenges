# Day 16 Challenge:
# Write a program to get the sum of n number? Eg. sum of 123 is 6.
# n is user entered value.

def allSum():
    n = input("Enter number: ")
    s = 0
    for x in n:
        s += int(x)
    print(s)


allSum()
