# Day 8 Challenge:
# On a certain day, the nurses at a hospital worked the following number of hours: Nurse Howard
# worked 8 hours; Nurse Pease worked 10 hours; Nurse Campbell worked 9 hours; Nurse Grace worked 8 hours; Nurse
# McCarthy worked 7 hours, and Nurse Murphy worked 12 hours. What is the average number of hours worked per nurse on
# this day? Average should be as a float value.


# thr = 0
# hr = [8, 10, 9, 8, 7, 12]
# all = len(hr)
# for i in hr:
#     thr += i
# print(thr / all)

def avgWork(a, b, c, d, e, f, nCount):
    totalHrs = float(a + b + c + d + e + f)
    avgHrs = totalHrs / nCount

    return avgHrs


nH = 8
nP = 10
nC = 9
nG = 8
nMC = 7
nM = 12
nurseCount = 6

avgHours = avgWork(nH, nP, nC, nG, nMC, nM, nurseCount)

print(avgHours)
