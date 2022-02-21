import sys

sys.stdin = open('input.txt')

num = int(input())
arr = list(map(int, input().split()))

ans = []
for i in range(num):
    ans.insert(arr[i], i+1)
ans.reverse()

print(*ans)