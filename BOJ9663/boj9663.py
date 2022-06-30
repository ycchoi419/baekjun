N = int(input())

cnt = 0


def sol(arr):
    global cnt
    # l번째 줄에 체스 말 놓기
    l = len(arr)
    if l == N:
        cnt += 1
        return
    for i in range(N):
        if i in arr:
            continue
        for k in range(l):
            if k+arr[k] == l+i:
                break
            elif k-arr[k] == l-i:
                break
        else:
            sol(arr + [i])

sol([])
print(cnt)