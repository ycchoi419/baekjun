import sys

sys.stdin = open('input.txt', 'r')

"""
검정색 영역을 set 자료형으로 만들어 len을 출력했다. 
각 영역은 네자리 정수로 표현하며 앞 두자리는 x좌표, 뒤 두자리는 y 좌표를 나타낸다. 
"""

num = int(input())

black_area = set()
for paper in range(num):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            black_area.add(100*(x+i)+y+j)

print(len(black_area))