import sys

sys.stdin = open('input.txt')

N = int(input())
arr = [[' ' for i in range(N)] for j in range(N)]


def sol(n, i, j):
    if n == 1:
        arr[i][j] = '*'
    else:
        a = n//3
        sol(a, i, j)
        sol(a, i+a, j)
        sol(a, i+2*a, j)
        sol(a, i, j+a)
        sol(a, i+2*a, j+a)
        sol(a, i, j+2*a)
        sol(a, i+a, j+2*a)
        sol(a, i+2*a, j+2*a)

sol(N, 0, 0)
for l in arr:
    print(''.join(l))
