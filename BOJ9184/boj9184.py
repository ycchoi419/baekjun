import sys

sys.stdin = open('input.txt')

w = [[[1 for i in range(21)] for j in range(21)] for k in range(21)]
for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b and b < c:
                w[a][b][c] = w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
            else:
                w[a][b][c] = w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]
ans = 0
while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1:
        break
    else:
        if a <= 0 or b <= 0 or c <= 0:
            ans = 1
        elif a > 20 or b > 20 or c > 20:
            ans = w[20][20][20]
        else:
            ans = w[a][b][c]

    print(f'w({a}, {b}, {c}) = {ans}')