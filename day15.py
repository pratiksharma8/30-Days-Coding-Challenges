# Day 15 Challenge:
# Lucille spent 12% of her weekly earnings on DVDs and deposited the rest into her savings account.
# If she spent $42 on DVDs, how much did she deposit into her savings account?

def expense():
    earn = 100
    exp = 12
    total_saved = earn - exp
    dvd_exp = 42
    s = (total_saved * dvd_exp) // exp

    print(f'She deposits ${s} on saving account')


expense()
