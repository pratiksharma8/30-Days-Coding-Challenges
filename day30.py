# Day 30 Challenge:
# Write a Python program that accepts two integers from the user and then prints the sum,
# the difference, the product, the average, the maximum (the larger of the two integers) and the minimum (smaller of
# the two integers).

def ganit():
    fNum = int(input('Enter first number: '))
    sNum = int(input('Enter second number: '))

    print(f'Sum of {fNum} and {sNum} is {fNum + sNum}')
    print(f'Difference of {fNum} and {sNum} is {abs(fNum - sNum)}')
    print(f'Product of {fNum} and {sNum} is {fNum * sNum}')
    print(f'Average of {fNum} and {sNum} is {(fNum + sNum) / 2}')

    if fNum != sNum:
        if fNum > sNum:
            print(f'Maximum between {fNum} and {sNum} is {fNum}')
            print(f'Minimum between {fNum} and {sNum} is {sNum}')
        else:
            print(f'Maximum between {fNum} and {sNum} is {sNum}')
            print(f'Minimum between {fNum} and {sNum} is {fNum}')
    else:
        print('The numbers are equal')


ganit()
