import sys

sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
asc = [1] * N
desc = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            asc[i] = max(asc[i], asc[j] + 1)
for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if A[i] > A[j]:
            desc[i] = max(desc[i], desc[j] + 1)
ans = 1
for i in range(N):
    ans = max(asc[i] + desc[i] - 1, ans)
print(ans)