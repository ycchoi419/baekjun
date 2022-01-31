from sys import stdin

# 예제 입력
stdin = open('input2304.txt', 'r')

# 입력 형식
num = int(stdin.readline())
columns = []
for T in range(num):
    columns.append(tuple(map(int, stdin.readline().split())))

# 기둥 순서대로 정렬 
columns.sort(key = lambda item: item[0])

# 최고 높이 구하기 : 최고 높이와 위치 찾기
max_height = 0 # 가장 높은 기둥의 높이
for index in range(len(columns)):
    if columns[index][1] > max_height:
        max_height = columns[index][1]
        max_index = index # 가장 높은 기둥의 순서 

# 최고 높이 기준으로 양쪽 넓이 구하기 
area = max_height
# max_index보다 작은 부분의 넓이 
local_height = 0 # 앞 기둥의 최고 높이 
for index in range(max_index):
    if columns[index][1] > local_height: # 앞 기둥 최고 높이보다 높은 경우 추가되는 넓이
        area += (columns[index][1] - local_height) * (columns[max_index][0] - columns[index][0])
        local_height = columns[index][1]
# max_index보다 큰 부분의 넓이 
local_height = 0 # 뒤 기둥의 최고 높이
for index in range(len(columns) - 1, max_index, -1): 
    if columns[index][1] > local_height: # 뒤 기둥 최고 높이보다 높은 경우 추가되는 넓이 
        area += (columns[index][1] - local_height) * (columns[index][0] - columns[max_index][0])
        local_height = columns[index][1]

# 출력 형식 
print(area)