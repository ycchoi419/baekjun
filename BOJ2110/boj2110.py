import sys
sys.stdin = open('input.txt')

N, C = map(int, sys.stdin.readline().split())
home = [0] * N
for i in range(N):
    home[i] = int(sys.stdin.readline())
home.sort()
start = 1
end = max(home)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    pos = home[0]
    for i in range(1, N):
        if home[i] - pos >= mid:
            cnt += 1
            pos = home[i]
            if cnt > C: break
    if cnt >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)