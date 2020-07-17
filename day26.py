# Day 26 Challenge:
# The temperature recorded at 8 A.M. is n °C. What is the equivalent of this temperature in degrees Fahrenheit?
# n is user entered value.

def c_to_f():
    cDegree = int(input("Enter the temperature in °C : "))
    fDegree = cDegree * (9.0 / 5.0) + 32
    print(
        f'The temperature recorded at 8 A.M. is {cDegree}°C. The equivalent of this temperature in degrees Fahrenheit is {fDegree}°F')


c_to_f()
