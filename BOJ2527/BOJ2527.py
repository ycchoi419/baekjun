import sys

sys.stdin = open('input.txt', 'r')


def rectangles(r1_x1, r1_y1, r1_x2, r1_y2, r2_x1, r2_y1, r2_x2, r2_y2):
    """
    x, y 축으로 projection 해서 나누어 생각한다. 
    0 * 점, 선 = 0
    점 * 점 = 점 
    점 * 선 = 선
    선 * 선 = 면
    
    겹치지 않을 때 0
    점으로 겹칠 때 1
    선으로 겹칠 때 10
    """
    # x축 projection
    if r1_x1 == r2_x2 or r1_x2 == r2_x1:  # x축 위에서 한 점에서 겹치는 경우 
        x = 1
    elif r1_x1 > r2_x2 or r1_x2 < r2_x1:  # x축 위에서 겹치지 않는 경우 
        x = 0
    else:  # 겹치는 구간이 존재하는 경우 
        x = 10

    # y축 projection
    if r1_y1 == r2_y2 or r1_y2 == r2_y1:  # y축 위에서 한 점에서 겹치는 경우 
        y = 1
    elif r1_y1 > r2_y2 or r1_y2 < r2_y1:  # y축 위에서 겹치지 않는 경우 
        y = 0
    else:
        y = 10

    # 정답 출력
    if x * y == 0:  # x, y 축 둘 중 하나라도 겹치지 않는 경우. 0 * 점 또는 선
        return 'd'
    elif x * y == 1: # 점 * 점 = 점
        return 'c'
    elif x * y == 10:  # 점 * 선 = 선
        return 'b'
    else:  # 선 * 선 = 면
        return 'a'


T = 4
for tc in range(1, T+1):
    r1_x1, r1_y1, r1_x2, r1_y2, r2_x1, r2_y1, r2_x2, r2_y2 = map(int, input().split())
    print(rectangles(r1_x1, r1_y1, r1_x2, r1_y2, r2_x1, r2_y1, r2_x2, r2_y2))