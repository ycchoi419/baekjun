from sys import stdin

# 예제 입력
stdin = open('input2477.txt', 'r')

# 입력받기
num = int(stdin.readline())
line = []
for i in range(6):
    line.append(tuple(map(int, stdin.readline().split())))

for i in range(6):
    if line[i][0] == line[(i + 2) % 6][0] and line[(i + 1) % 6][0] == line[(i + 3) % 6][0]:
        area = line[(i + 4) % 6][1] * line[(i + 5) % 6][1] - line[(i + 1) % 6][1] * line[(i + 2) % 6][1]

# 출력하기
print(area * num)