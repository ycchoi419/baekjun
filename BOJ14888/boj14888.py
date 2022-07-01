import sys
from itertools import permutations

sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, division = map(int, input().split())
operations = [0] * plus + [1] * minus + [2] * multiply + [3] * division
my_max = -1000000000
my_min = 1000000000
for i in permutations(operations):
    tmp = numbers[0]
    for j in range(N - 1):
        if i[j] == 0:
            tmp += numbers[j+1]
        elif i[j] == 1:
            tmp -= numbers[j+1]
        elif i[j] == 2:
            tmp *= numbers[j+1]
        elif i[j] == 3:
            if tmp < 0 < numbers[j + 1]:
                tmp = -(-tmp//numbers[j+1])
            else:
                tmp //= numbers[j+1]
    my_min = min(my_min, tmp)
    my_max = max(my_max, tmp)

print(my_max)
print(my_min)