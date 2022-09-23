import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in trees:
        if i > mid:
            cnt += i - mid
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1
print((start + end) // 2)