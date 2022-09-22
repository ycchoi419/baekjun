# N = int(input())
# ans = []
# def sol(A, N1, N2):
#     N3 = 6 - N1 - N2
#     global cnt
#     """
#     N1번째 장대에 있는 A층 탑을 N2번째로 옮김
#     """
#     if A == 1:
#         ans.append([N1, N2])
#         return
#     sol(A-1, N1, N3)
#     ans.append([N1, N2])
#     sol(A-1, N3, N2)
#
# sol(N, 1, 3)
# print(len(ans))
# for i in ans:
#     print(*i)

N = int(input())
print(2**N-1)

def sol(A, N1, N2):
    N3 = 6 - N1 - N2
    global cnt
    """
    N1번째 장대에 있는 A층 탑을 N2번째로 옮김
    """
    if A == 1:
        print(N1, N2)
        return
    sol(A-1, N1, N3)
    print(N1, N2)
    sol(A-1, N3, N2)

sol(N, 1, 3)