# Day 1 Challenge:
# There was a teacher in a small town who loves coding and he wants to create a program which prints
# out the whole multiplication table of an entered number for his students. Can you help him to write a program in
# Python?

def multiplication_table():
    num = int(input('Enter number to print the multiplication table: '))

    for x in range(1, 11):
        print(f'{num} X {x} = {num * x}')


multiplication_table()
