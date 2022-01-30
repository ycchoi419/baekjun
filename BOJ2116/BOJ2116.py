from sys import stdin

#입력 예시
stdin = open('input2116.txt', 'r')

# 입력
num = int(stdin.readline())
dices = []
for i in range(num):
    dices.append(tuple(map(int, stdin.readline().split())))

def opposite(face, dice):
# dice에서 num 반대편에 있는 숫자를 반환 
    for i in range(len(dice)):
        if face == dice[i]:
            if i == 0:
                return dice[5]
            elif i == 5:
                return dice[0]
            elif i == 1:
                return dice[3]
            elif i == 3:
                return dice[1]
            elif i == 2:
                return dice[4]
            else:
                return dice[2]
        else: 
            continue
max_value = 0
for i in range(6):
    face = dices[0][i]
    total = 0
    n = 0
    while n < num:
        # 현재 숫자와 반대편 숫자가 5와 6인 경우 
        if min(face, opposite(face, dices[n])) == 5:
            total += 4
        # 현재 숫자와 반대편 숫자 중 하나가 6인 경우 
        elif max(face, opposite(face, dices[n])) == 6:
            total += 5
        else:
            total += 6
        face = opposite(face, dices[n])
        n += 1
    max_value = max(total, max_value)
print(max_value)
