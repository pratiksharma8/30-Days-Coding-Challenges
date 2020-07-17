# Day 4 Challenge:
# Jack bought 400 hot dogs for the school picnic.
# If they were contained in packages of 8 hotdogs, how many total packages did he buy?
# Create a Python program without using \ or % operator.

def total_hotdog():
    n = 400
    pack = 0
    for x in range(1, n + 1):
        if n >= 8:
            pack += 1
            n -= 8
    print(pack)


total_hotdog()
