import sys

sys.stdin = open('input.txt')

N = int(input())

stack = []
for _ in range(N):
    a = input()
    if a.startswith('push'):
        stack.append(int(a[4:]))
    elif a == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a == 'size':
        print(len(stack))
    elif a == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif a == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        continue