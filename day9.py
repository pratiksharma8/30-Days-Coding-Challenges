# Day 9 Challenge:
# Mr Richard Tupper is purchasing gifts for his family. So far he has purchased the following:
# ■ 3 sweaters, each valued at $68
# ■ 1 computer game valued at $75
# ■ 2 bracelets, each valued at $43
# Later, he returned one of the bracelets for a full
# refund and received a $10 rebate on the computer game. What is the total cost of the gifts
# after the refund and rebate?
# Calculation part of the program should be under three lines.

sweater = 68
computer = 75
bracelet = 43

total = 3 * sweater + 1 * computer + 2 * bracelet
refund = total - 1 * bracelet - 10
print(refund)
