# Day 17 Challenge:
# There are 10 students in a class some students names are same to other students, print the names
# that occur more than one time. All names should be in a single string.
# Eg. str = “Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar Arjun Nakul Ankit Deepak Deepak Amit Sagar”

students = 'Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar Arjun Nakul Ankit Deepak Deepak Amit Sagar'
s = students.split(' ')
z = [x for x in s if s.count(x) > 1]
z = list(set(z))
z = ' '.join(z)
print(z)

