import sys

sys.stdin = open('input.txt', 'r')

width, height = map(int, input().split())

T = int(input())

shops = [0] * T

def get_position(direction, length):
    """
    왼쪽 상단 점을 기준으로 시계방향으로 측정한 거리가 위치가 된다.
    else를 쓰지 않을 경우 nameError가 발생할 수 있다.
    """
    if direction == 1:
        ans = length
    elif direction == 2:
        ans = 2*width + height - length
    elif direction == 3:
        ans = 2*width + 2*height - length
    elif direction == 4:
        ans = width + length
    else:
        ans = 0
    return ans

# 각 상점의 위치 구하기
for i in range(T):
    direction, length = map(int, input().split())
    position = get_position(direction, length)
    shops[i] = position

# 동근이 위치 구하기
dg_direction, dg_length = map(int, input().split())
dg_position = get_position(dg_direction, dg_length)

circumference = 2*width + 2*height

min_length = 0
for i in range(T):
    # 시계방향 또는 반시계방향의 거리 중 작은 것을 min_length에 추가
    min_length += min((dg_position-shops[i])%circumference, circumference - ((dg_position-shops[i])%circumference))

print(min_length)