import sys

sys.stdin = open('input.txt')

def max_temp(N, K, temp):
    maximum = sum(temp[:K])
    next_sum = maximum
    for i in range(N-K): 
        next_sum = next_sum - temp[i] + temp[i+K]
        maximum = max(maximum, next_sum)
    return maximum


N, K = tuple(map(int, input().split()))
temp = list(map(int, input().split()))
ans = max_temp(N, K, temp)
print(ans)