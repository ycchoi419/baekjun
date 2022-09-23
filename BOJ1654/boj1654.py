import sys
sys.stdin = open('input.txt')

K, N = map(int, input().split())
nums = [0] * K
for i in range(K):
    nums[i] = int(input())
ans = 0
start = 1
end = max(nums)
mid = (start + end) // 2
while start <= end:
    ans = mid
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += nums[i] // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print((start + end)//2)