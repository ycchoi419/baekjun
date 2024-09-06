import sys 

sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    for i in range(2, b+1):
        if (a**i)%10 == a%10:
            b = b % (i-1)
            if b == 0: b = i - 1
            break
    print((a ** b - 1) % 10 + 1)