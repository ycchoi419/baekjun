from sys import stdin

stdin = open('input.txt')


# def quick_sort(p, r):
#     global arr
#     if p < r:
#         q = partition(p, r)
#         quick_sort(p, q-1)
#         quick_sort(q+1, r)


# def partition(p, r):
#     global arr
#     x = arr[r]
#     i = p-1
#     for j in range(p, r):
#         if arr[j] < x:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[r] = arr[r], arr[i+1]
#     return i+1


N = int(stdin.readline())
arr = [0] * N
for i in range(N):
    arr[i] = int(stdin.readline())

arr.sort()

for i in arr:
    print(i)