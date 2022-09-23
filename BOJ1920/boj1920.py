import sys

sys.stdin = open('input.txt')

N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
inputs = list(map(int, input().split()))
for i in inputs:
    start = 0
    end = N - 1
    ans = 0
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == i:
            ans = 1
            break
        elif nums[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    print(ans)