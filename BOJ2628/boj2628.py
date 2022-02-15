import sys

sys.stdin = open('input.txt')

width, height = map(int, input().split())
num = int(input())
width_arr = [0, width]
height_arr = [0, height]

for _ in range(num):
    dir, pnt = map(int, input().split())
    if dir:
        width_arr.append(pnt)
    else:
        height_arr.append(pnt)
width_arr.sort()
height_arr.sort()

width_max = 0
height_max = 0
for i in range(len(width_arr)-1):
    width_max = max(width_max, width_arr[i+1] - width_arr[i])
for i in range(len(height_arr)-1):
    height_max = max(height_max, height_arr[i+1] - height_arr[i])

print(width_max * height_max)