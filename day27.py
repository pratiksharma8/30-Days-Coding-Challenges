# Day 27 Challenge:
# Write a Python program to input centimeter and convert to inch, meter and kilometer.

def len_converter():
    centi = int(input('Enter length in cm: '))
    inch = centi / 2.54
    meter = centi / 100
    km = centi / 100000
    print(f'{centi} cm is {inch} inch, {meter} m and {km} km')


len_converter()
