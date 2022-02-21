import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split())
room = [0] * 12
for i in range(N):
    S, Y = map(int, input().split())
    room[S + 2*(Y-1)] += 1
ans = 0
for i in room:
    ans += (i + K - 1)//K
print(ans)