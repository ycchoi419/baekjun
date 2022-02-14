import sys

sys.stdin = open('input.txt')


def bingo(board, nums):
    """
    몇 번째 숫자에서 3빙고가 완성되는지 찾는다.
    :param board: 철수 빙고판 2차원 list
    :param nums: 숫자 불리는 순서대로 1차원 list
    :return: 몇 번 불렸을 때 3빙고인지
    """
    num_list = [0] * 26  # 각 숫자들이 속한 행, 열, 대각선 0~4는 행 5~9는 열 10, 11은 대각선
    check_bingo = [0] * 12  # 각 행, 열, 대각선에 있는 숫자가 몇 번 불렸는지 확인 5가되면 1빙고
    cnt = 0  # 빙고 수. 3이되면 끝
    for i in range(5):
        for j in range(5):
            num_list[board[i][j]] = [i, j + 5]  # 몇 번째 행 또는 열에 포함되는지
            if i == j:  # / 대각선
                num_list[board[i][j]].append(10)
            if i + j == 4:  # \ 대각선
                num_list[board[i][j]].append(11)

    for i in range(len(nums)):
        for num in num_list[nums[i]]:
            check_bingo[num] += 1
            if check_bingo[num] == 5:
                cnt += 1
            if cnt == 3:
                return i + 1
    return 25


cs = [list(map(int, input().split())) for _ in range(5)]  # 빙고판 5*5 list

num_call = []  # 사회자가 부르는 숫자들의 1차원 list
for i in range(5):
    num_call.extend(list(map(int, input().split())))

print(bingo(cs, num_call))
