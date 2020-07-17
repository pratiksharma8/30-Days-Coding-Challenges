# Day 6 Challenge:
# A floppy disk shows f bytes free and u bytes used.
# If you delete a file of size o bytes and create a new file of size
# n bytes, how many free bytes will the floppy disk have?
# f u o and n are user-entered value.

def free_bytes():
    f = int(input('Enter Free Bytes: '))
    u = int(input('Enter Used Bytes: '))

    total = f + u
    print(f'Total size : {total} bytes')

    o = int(input('Enter Bytes to Delete: '))
    free = total - (u - o)
    print(f'Free size : {free} bytes')

    n = int(input('Enter Bytes to Create: '))
    new_free = free - n
    print(f'Free size : {new_free} bytes')


free_bytes()
