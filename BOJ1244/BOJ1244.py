from sys import stdin

# 입력 예시
#stdin = open('input1244.txt', 'r')

# 입력 받기
num = int(stdin.readline())
switches = list(map(int,stdin.readline().split()))
T = int(stdin.readline())
students = []

# test case
while T > 0:
    students.append(tuple(map(int,stdin.readline().split())))
    T -= 1

# 스위치를 바꿔주는 함수 
def turnswitch(num):
    if num:
        return 0
    else:
        return 1

for student in students:
    # 남학생인 경우 
    if student[0] == 1:
        for switch_index in range(len(switches)):
            # 배수인 경우 turn_switch
            if (switch_index + 1) % student[1] == 0:
                switches[switch_index] = turnswitch(switches[switch_index])
    
    # 여학생인 경우 
    if student[0] == 2:
        i = 0
        while True:
            # index를 넘어간 경우
            if student[1] + i > num or student[1] - i < 1:
                break
            # 가장 가운데 있는 스위치
            if i == 0:
                switches[student[1] - 1] = turnswitch(switches[student[1] - 1])
                i += 1
            # 양쪽이 같은 경우 둘 다 turn_switch
            elif switches[student[1] - 1 + i] == switches[student[1] - 1 - i]:
                switches[student[1] - 1 + i] = turnswitch(switches[student[1] - 1 + i])
                switches[student[1] - 1 - i] = turnswitch(switches[student[1] - 1 - i])
                i += 1
            # 양쪽이 다른 경우 
            else: 
                break

# 출력 형식 
for j in range(num):
    if (j + 1) % 20 == 0:
        print(switches[j])
    elif j == num - 1:
        print(switches[j], end = '')
    else: 
        print(switches[j], end = ' ')
