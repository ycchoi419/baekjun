import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(N)]
