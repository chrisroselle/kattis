import sys

target = int(input())

def make_odd(half):
    return half + half[::-1][1:]

def make_even(half):
    return half + half[::-1]
    
n = 1
while (True):
    squared = 2 ** n
    # print('n={} squared={} target={}'.format(n, squared, target))
    if (target > squared):
        target = target - squared
        n = n + 1
    else:
        if (target - (squared/2) > 0):
            # print('first half')
            target = target - squared
            base_ten = 2 ** n + target - 1
            # print('base_ten={}'.format(base_ten))
            print(int(make_even(bin(base_ten)[2:]),2))
            break
        else:
            # print('second half')
            base_ten = 2 ** (n-1) + target - 1
            # print('base_ten={}'.format(base_ten))
            print(int(make_odd(bin(base_ten)[2:]),2))
            break