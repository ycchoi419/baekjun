import sys

sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    nA, *A = map(int, input().split())
    nB, *B = map(int, input().split())
    arrA = [0]*4
    arrB = [0]*4
    for aa in A:
        arrA[aa-1] += 1
    for bb in B:
        arrB[bb-1] += 1

    for i in range(3, -1, -1):
        if arrA[i] > arrB[i]:
            print('A')
            break
        elif arrA[i] < arrB[i]:
            print('B')
            break
        else:
            continue
    else:
        print('D')
