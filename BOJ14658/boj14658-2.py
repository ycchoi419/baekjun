import sys

sys.stdin = open('input.txt')

N, M, L, K = map(int, input().split())
x = [0] * K
y = [0] * K
for i in range(K):
    x[i], y[i] = map(int, input().split())
ans = 0
for i in range(K):
    for j in range(K):
        cnt = 0
        for k in range(K):
            if x[i] <= x[k] <= x[i] + L + 1 and y[j] <= y[k] <= y[j] + L + 1:
                cnt += 1
        ans = max(ans, cnt)
ans = K - ans
print(ans)