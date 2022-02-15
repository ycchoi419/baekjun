import sys

sys.stdin = open('input.txt')

num = int(input())
ans = [num]
for i in range(num, num//2-1, -1):
    arr = [num, i]
    while arr[-2] - arr[-1] >= 0:
        arr.append(arr[-2] - arr[-1])
    if len(arr) > len(ans):
        ans = arr

print(len(ans))
print(*ans)