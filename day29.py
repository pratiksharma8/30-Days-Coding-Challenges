# Day 29 Challenge:
# Write a Python program to takes the user for a distance (in meters) and the time was taken
# (as three numbers: hours, minutes, seconds), and display the speed, in miles per hour.

def miles_per_hr():
    mDistance = int(input('Enter distance in meters: '))
    hrTime = int(input('Enter time (hr): '))
    mTime = int(input('Enter time (min): '))
    sTime = int(input('Enter time (s): '))

    m_to_miles = mDistance / 1609
    total_time_in_hr = hrTime + (mTime / 60) + (sTime / 3600)
    total_MperHr = m_to_miles / total_time_in_hr

    print(f'It takes {total_MperHr} miles per hour to complete {mDistance} m in {hrTime} hr {mTime} min {sTime} s')


miles_per_hr()
