import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
memo = [1]*N  # Ai 에서 끝나는 최장증가부분수열의 최댓값
for i in range(1, N):
    for k in range(i):
        if A[k] < A[i]:
            memo[i] = max(memo[i], memo[k]+1)
print(max(memo))
