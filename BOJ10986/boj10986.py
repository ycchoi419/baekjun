from sys import stdin

stdin = open('input.txt')

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
add = [0 for _ in range(N+1)]
for i in range(1, N+1):
    add[i] = (add[i-1] + arr[i-1]) % M
ans = 0
cnt = [0 for _ in range(M)]
for i in add:
    cnt[i] += 1
for i in cnt:
    ans += i*(i-1)//2
print(ans)