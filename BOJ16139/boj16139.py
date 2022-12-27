import sys

sys.stdin = open('input.txt')

S = sys.stdin.readline().rstrip()
cnt = [[0 for i in range(len(S) + 1)] for j in range(26)]
for i in range(len(S)):
    cnt[ord(S[i]) - ord('a')][i] += 1
for i in range(26):
    for j in range(1, len(S)):
        cnt[i][j] = cnt[i][j-1] + cnt[i][j]
N = int(input())
for _ in range(N):
    c, i, j = sys.stdin.readline().split()
    print(cnt[ord(c) - ord('a')][int(j)] - cnt[ord(c) - ord('a')][int(i) - 1])
