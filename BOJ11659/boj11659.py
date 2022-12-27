from sys import stdin

stdin = open('input.txt')

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
add = [0 for _ in range(N+1)]
for i in range(N):
    add[i+1] = add[i] + arr[i]
for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(add[j]-add[i-1])