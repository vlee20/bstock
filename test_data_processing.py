import pytest

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

def test_get_avg():
    assert get_avg([1, 2, 3]) == '2.00'
    assert get_avg([1.5, 2.5, 3.5]) == '2.50'
    assert get_avg([0, 0, 0]) == '0.00'
    assert get_avg([-1, -2, -3]) == '-2.00'
    assert get_avg([1]) == '1.00'
    assert get_avg([]) == None  # Handle empty list case
    
def test_get_sum():
    assert get_sum([1, 2, 3]) == 6
    assert get_sum([1.5, 2.5, 3.5]) == 7.5
    assert get_sum([0, 0, 0]) == 0
    assert get_sum([-1, -2, -3]) == -6
    assert get_sum([1]) == 1
    assert get_sum([]) == 0  # Handle empty list case