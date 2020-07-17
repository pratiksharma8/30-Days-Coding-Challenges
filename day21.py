# Day 21 Challenge:
# Write a program that for a given hour and minutes values calculates an angle in degrees between
# the hour and the minute hands. Check whether the minute hand overlapping the hour hand at a given time.

def time_degree():
    hr = input("Enter hour hand : ")
    m = input("Enter minute hand: ")
    one_deg = 30
    diff = abs(int(hr) - int(m))
    if int(hr) < 0 or int(m) < 0 or int(hr) > 12 or int(m) > 12:
        print('Wrong input')

    print(f'{(diff * one_deg)} Degrees')


time_degree()

# def calcAngle(h, m):
#     if h < 0 or m < 0 or h > 12 or m > 60:
#         print('Wrong input')
#
#     if h == 12:
#         h = 0
#     if m == 60:
#         m = 0
#     hour_angle = 0.5 * (h * 60 + m)
#     minute_angle = 6 * m
#     angle = abs(hour_angle - minute_angle)
#     angle = min(360 - angle, angle)
#
#     return int(angle)
#
#
# h = int(input("Enter hour (1-12).."))
# m = int(input("Enter minute (0-59).."))
# clockAngle = calcAngle(h, m)
# if clockAngle == 0:
#     print("hour and minute hands overlaps")
# else:
#     print(clockAngle, "degree")
