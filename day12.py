# Day 12 Challenge:
# The number of red blood corpuscles in one the cubic millimetre is about 5,000,000 and the number
# of white blood corpuscles in one cubic the millimetre is about 8,000. What, then, is the ratio of white blood
# corpuscles to red blood Corpuscles? Aspect Ratio should be as an int value.

def greatestCommonFactor(whiteC, redC):
    return whiteC if (redC == 0) else greatestCommonFactor(redC, whiteC % redC)


rbc = 5000000
wbc = 8000

factor = greatestCommonFactor(wbc, rbc)

whiteRatio = int(wbc / factor)
redRatio = int(rbc / factor)

print(f"{whiteRatio}:{redRatio}")
