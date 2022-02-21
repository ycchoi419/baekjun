# import sys
# # 부분 정답
#
# sys.stdin = open('input.txt')
#
#
# N = int(input())
#
# plane = [[0] * 1001 for _ in range(1001)]
# ans = [0] * N
# for num in range(1, N+1):
#     x, y, width, height = map(int, input().split())
#
#     for i in range(y, y + height):
#         for j in range(x, x + width):
#             if plane[i][j]:
#                 ans[plane[i][j]-1] -= 1
#                 plane[i][j] = num
#             else:
#                 plane[i][j] = num
#             ans[num-1] += 1
# for i in ans:
#     print(i)


# import sys
#
# sys.stdin = open('input.txt')
#
# N = int(input())
# ans = [[] for _ in range(N)]
#
# for num in range(N):
#     x, y, width, height = map(int, input().split())
#     for xx in range(x, x+width):
#         for yy in range(y, y+height):
#             for i in range(num):
#                 if (xx, yy) in ans[i]:
#                     ans[i].remove((xx, yy))
#             ans[num].append((xx, yy))
#
# for i in ans:
#     print(len(i))

