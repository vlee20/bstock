def get_avg(n):
    tot = 0
    for i in n:
        tot += float(i)
    return '{:,.2f}'.format(tot/len(n)) if len(n) > 0 else None

def get_sum(n):
    tot = 0
    for i in n:
        tot += i
    return tot