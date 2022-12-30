N, M = map(int, input().split())

arr = [0 for _ in range(M)]


def sol(i):
    if i == M:
        print(*arr)
        return
    for j in range(N):
        arr[i] = j + 1
        sol(i+1)


sol(0)

