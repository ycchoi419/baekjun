from sys import stdin

# 예제 입력 
stdin = open('input2491.txt', 'r')

# 입력 받기
num = int(stdin.readline())
series = tuple(map(int, stdin.readline().split()))

# 커지는 경우 
max_len = 1
length = 1
for i in range(1, len(series)):
    if series[i] >= series[i - 1]:
        length += 1
    else:
        max_len = max(max_len, length)
        length = 1
max_len = max(max_len, length)

# 작아지는 경우 
min_len = 1
length = 1
for i in range(1, len(series)):
    if series[i] <= series[i - 1]:
        length += 1
    else:
        min_len = max(min_len, length)
        length = 1
min_len = max(min_len, length)

# 출력 형식 
print(max(max_len, min_len))