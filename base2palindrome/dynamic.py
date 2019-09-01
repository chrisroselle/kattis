import sys, math

def next(current):
    length = len(current)
    # print('current = {} - length {}'.format(current, length))
    if length % 2 == 0:
        # even
        # print('length = {}   [{},{},-1]'.format(length, length//2 - 1, 0))
        for i, value in enumerate(current[length//2 - 1:0:-1]):
            # print('i={} value={}'.format(i, value))
            if value == "0":
                half = current[0:length//2 - i - 1] + "1" + "0" * i
                # print('half = {}'.format(half))
                # print('rest = {}'.format(half[::-1]))
                return half + half[::-1]
            i = i + 1
        return "1" + "0" * (length - 1) + "1"
    else:
        # odd
        # print('length = {}   [{},{},-1]'.format(length, math.ceil(length/2) - 1, 0))
        for i, value in enumerate(current[math.ceil(length/2) - 1:0:-1]):
            # print('i={} value={}'.format(i, value))
            if value == "0":
                half = current[0:length//2 - i] + "1" + "0" * i
                # print('half = {}'.format(half))
                # print('rest = {}'.format(half[::-1][1:]))
                return half + half[::-1][1:]
            i = i + 1
        return "1" + "0" * (length - 1) + "1"
    
    
    
palindromes = {}
palindromes[1] = "1"

target = int(input())

for i in range(2, target + 1):
    palindromes[i] = next(palindromes[i-1])

# print('palindromes: {}'.format(palindromes))
print(int(palindromes[target], 2))