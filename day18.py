# Day 18 Challenge:
# Lefty keeps track of the length of each fish that he catches. Below are the lengths in inches of
# the fish that he caught one day: 12, 13, 8, 10, 17 What is the largest fish length that Lefty caught that day?
# Solve without using conditional statements and the loop.

def bigFish(arr):
    print(max(arr))

    arr.sort()
    print(arr[-1])


bigFish([12, 13, 8, 10, 17])
