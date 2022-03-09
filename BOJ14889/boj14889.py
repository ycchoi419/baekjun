import sys
from itertools import combinations

sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
min_diff = 9999
for team_start in combinations(range(N), N//2):
    start_sum = link_sum = 0
    team_link = []
    for i in range(N):
        if i in team_start:
            continue
        else:
            team_link.append(i)
    for i in team_start:
        for j in team_start:
            start_sum += arr[i][j]
    for i in team_link:
        for j in team_link:
            link_sum += arr[i][j]
    min_diff = min(min_diff, abs(link_sum-start_sum))
print(min_diff)