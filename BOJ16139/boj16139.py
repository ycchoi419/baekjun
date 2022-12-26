import sys

sys.stdin = open('input.txt')

S = input()
cnt = [[0 for i in range(len(S) + 1)] for j in range(26)]
for i in range(len(S)):
    cnt[ord(S[i]) - ord('a')][i] += 1
for i in range(26):
    for j in range(1, len(S)):
        cnt[i][j] = cnt[i][j-1] + cnt[i][j]
# print(cnt)
N = int(input())
for _ in range(N):
    c, i, j = input().split()
    # print(int(j))
    # print(int(i))
    # print(ord(c) - ord('a'))
    print(cnt[ord(c) - ord('a')][int(j)] - cnt[ord(c) - ord('a')][int(i) - 1])
