N = int(input())

for _ in range(N):
    print('*', end='')
    print(' *'*((N-1)//2))
    print(' *'*(N//2))