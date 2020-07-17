# Day 13 Challenge:
# 5th graders Kara and Rani both have lemonade stands. Kara sells her lemonade at 5 cents a glass
# and Rani sells hers at 7 cents a glass. Kara sold k number of glasses of lemonade today and Rani sold r number of
# glasses. Who made the most money and by what amount? k and r are user-entered value.

def lemonade():
    kara = 5
    rani = 7

    k_sales = input("How many glasses did Kara sell? : ")
    r_sales = input("How many glasses did Rani sell? : ")

    kara_profit = kara * int(k_sales)
    rani_profit = rani * int(r_sales)

    if kara_profit > rani_profit:
        print(f'Kara made ${kara_profit - rani_profit} more than Rani')
    elif kara_profit < rani_profit:
        print(f'Rani made ${rani_profit - kara_profit} more than Kara')
    else:
        print('Both made equal amount of profit')


lemonade()
