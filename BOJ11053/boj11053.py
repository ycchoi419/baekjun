import sys

sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
nums = sorted(list(set(A)))
C = [[0] * (len(nums)+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, len(nums)+1):
        if nums[j-1]==A[i-1]:
            C[i][j] = C[i-1][j-1]+1
        else:
            C[i][j] = max(C[i-1][j], C[i][j-1])
print(C[-1][-1])