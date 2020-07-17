# Day 3 Challenge:
# A chef was cooking something special which required exact 200ml water but he doesn’t have 200ml
# cup he has a 500ml cup and a 300ml cup but that dish required exactly 200ml water. Can you solve this problem in
# Python?

def cook():
    bCup = 500
    sCup = 300
    print(f'Fill big cup to full. {bCup} ml')
    print(f'Pour big cup of {bCup} ml to fill empty cup of {sCup} ml and he is left with {bCup - sCup} ml in big cup')
    print('Chef is Happy 😁')


cook()
