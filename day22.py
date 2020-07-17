# Day 22 Challenge:
# Write a Python Program to Find if a given Year is a Leap Year or not.

def leap_year():
    year = int(input('Enter Year: '))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a Leap Year')
            else:
                print(f'{year} is not a Leap Year')
        else:
            print(f'{year} is a Leap Year')
    else:
        print(f'{year} is not a Leap Year')


leap_year()
