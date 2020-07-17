# Day 25 Challenge:
# Write a Python method to check whether a string is a valid password.
# Password rules:
# Should have at least one number.
# Should have at least one uppercase and one lowercase character.
# Should have at least one special symbol.
# Should be between 6 to 20 characters long.

def check_password():
    spec_char = ['!', '@', '#', '$', '%', '&']
    password = input('Input Password: ')
    val = True

    if len(password) > 20 or len(password) < 6:
        print("INVALID PASSWORD: Must have at least 6 characters and not more than 20 characters")
        val = False

    if " " in password:
        print("INVALID PASSWORD: Must not have spaces")
        val = False

    if not any(x.isupper() for x in password):
        print("INVALID PASSWORD: Must have at least one uppercase character")
        val = False

    if not any(x.islower() for x in password):
        print("INVALID PASSWORD: Must have at least one lowercase character")
        val = False

    if not any(x.isdigit() for x in password):
        print("INVALID PASSWORD: Must have at least one numeric character")
        val = False

    if not any(x in spec_char for x in password):
        print("INVALID PASSWORD: Must have at least one special character. i.e: '!', '@', '#', '$', '%', '&'")
        val = False

    if val:
        print("VALID PASSWORD")


check_password()
