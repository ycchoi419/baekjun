import sys

sys.stdin = open('input.txt')

C, R = map(int, input().split())
N = int(input())

def seats(C, R, N):
    if N > C * R:
        return 0
    direction = 0  # 0:오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    di = [0, 1, 0, -1]  # 오른, 아래, 왼, 위 순서대로 i 방향 move
    dj = [1, 0, -1, 0]  # 오른, 아래, 왼, 위 순서대로 j 방향 move
    my_arr = [[0] * R for _ in range(C)]  # N*N list
    i, j = 0, 0
    for n in range(1, N):
        my_arr[i][j] = n
        if ((i + di[direction]) in range(C)) and ((j + dj[direction]) in range(R)) and not (
                my_arr[i + di[direction]][j + dj[direction]]):
                pass
        else:
            # 이미 숫자가 채워져 있거나 인덱스를 벗어날 때 방향 전환
            direction = (direction + 1) % 4
        i += di[direction]
        j += dj[direction]
    return '{} {}'.format(i+1, j+1)


print(seats(C, R, N))