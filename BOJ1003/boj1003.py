T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_zero = [0] * (N+1)
    num_zero[0] = 1
    for i in range(2, N+1):
        num_zero[i] = num_zero[i-2] + num_zero[i-1]
    num_one = [0] * (N+1)
    if N:
        num_one[1] = 1
    for i in range(2, N+1):
        num_one[i] = num_one[i-2] + num_one[i-1]
    print(f'{num_zero[N]} {num_one[N]}')