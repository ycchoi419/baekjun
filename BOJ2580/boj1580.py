import sys
import pprint

sys.stdin = open('input.txt')

sudoku = [list(map(int, input().split())) for _ in range(9)]
ivisited = [[0 for _ in range(10)] for __ in range(9)]
jvisited = [[0 for _ in range(10)] for __ in range(9)]
svisited = [[0 for _ in range(10)] for __ in range(9)]

blank = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j]:
            ivisited[i][sudoku[i][j]] = 1
            jvisited[j][sudoku[i][j]] = 1
            svisited[(i//3)*3 + j//3][sudoku[i][j]] = 1
        else:
            blank.append((i, j))

def sol(k):
    if k == len(blank):
        for l in sudoku:
            print(*l)
        exit(0)
    else:
        i, j = blank[k]
        for x in range(1, 10):
            if ivisited[i][x] or jvisited[j][x] or svisited[(i//3)*3 + j//3][x]:
                continue
            else:
                ivisited[i][x] = 1
                jvisited[j][x] = 1
                svisited[(i//3)*3 + j//3][x] = 1
                sudoku[i][j] = x
                sol(k+1)
                ivisited[i][x] = 0
                jvisited[j][x] = 0
                svisited[(i//3)*3 + j//3][x] = 0
                sudoku[i][j] = 0

sol(0)