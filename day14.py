# Day 14 Challenge:
# How many ways can four students Ram Anuj Deepak and Ravi line up in a line, if the order matters?
# Print all possible combination.

import itertools


def maxorder():
    students = itertools.permutations(['Ram', 'Anuj', 'Deepak', 'Ravi'])
    for i in students:
        print([', '.join(i)])


maxorder()

# def maxorder(arr):
#     if len(arr) == 0:
#         return []
#
#     if len(arr) == 1:
#         return [arr]
#
#     l = []
#     for i in range(len(arr)):
#         m = arr[i]
#         remLst = arr[:i] + arr[i + 1:]
#         for p in maxorder(remLst):
#             l.append([m] + p)
#     return l
#
#
# sArr = ['Ram', 'Anuj', 'Deepak', 'Ravi']
# for c in maxorder(sArr):
#     print(c)
