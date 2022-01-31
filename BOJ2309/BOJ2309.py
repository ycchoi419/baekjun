from sys import stdin 

# 예제 입력
stdin = open('input2309.txt', 'r')

# 입력 형식
dwarfs = []
for i in range(9):
    dwarfs.append(int(stdin.readline()))

sum_age = sum(dwarfs)

# 전체 합에서 두 난쟁이 키를 뺐을 때 100이 되는 두 난쟁이를 찾는다. 
for d1 in range(9):
    for d2 in range(d1 + 1, 9):
        if sum_age == dwarfs[d1] + dwarfs[d2] + 100:
            dwarfs.pop(d2)
            dwarfs.pop(d1)
            break
    if len(dwarfs) == 7:
        break

# 출력 형식
dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)