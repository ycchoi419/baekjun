import sys

N, M = map(int, input().split())
visited = [0 for _ in range(N+1)]
arr = [0] * M
mcnt = 0
ncnt = 1
while True:
    if mcnt == M:
        print(*arr)
        mcnt -= 1
        visited[arr[mcnt]] = 0
        ncnt = arr[mcnt] + 1
        continue
    if ncnt > N:
        mcnt -= 1
        if mcnt < 0:
            break
        ncnt = arr[mcnt] + 1
        visited[arr[mcnt]] = 0
    else:
        if not visited[ncnt]:
            visited[ncnt] = 1
            arr[mcnt] = ncnt
            mcnt += 1
            continue
        else:
            ncnt += 1