import sys
sys.stdin = open('input.txt')
N = int(input())
nums = list(map(int, input().split()))
nums_dict = dict()
for i in nums:
    if i in nums_dict:
        nums_dict[i] += 1
    else:
        nums_dict[i] = 1
M = int(input())
ans = [0] * M
inputs = list(map(int, input().split()))
for i in range(M):
    ans[i] = nums_dict.get(inputs[i]) or 0
print(*ans)