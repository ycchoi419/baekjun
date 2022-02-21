import sys

sys.stdin = open('input.txt')


w, h = map(int, input().split())
x, y = map(int, input().split())
hrs = int(input())
x = (x + hrs)%(2*w)
y = (y + hrs)%(2*h)
print((x+2*(x//w)*(w-x)), (y+2*(y//h)*(h-y)))
