import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())
ladders = dict()
snakes = dict()

for _ in range(N):
    a, b = map(int, input().split())
    ladders.update({a: b})
for _ in range(M):
    a, b = map(int, input().split())
    snakes.update({a: b})

def sol():
    q = deque()
    q.append(1)
    tmp = deque()
    cnt = 0
    while True:
        while q:
            position = q.popleft()
            max_i = 0
            for i in range(1, 7):
                if position+i == 100:
                    return cnt + 1
                    break
                if position+i in ladders:
                    tmp.append(ladders.get(position+i))
                elif position+i in snakes:
                    tmp.append(snakes.get(position+i))
                else:
                    max_i = i
            tmp.append(position+max_i)
        q.extend(tmp)
        tmp.clear()
        cnt += 1

print(sol())
