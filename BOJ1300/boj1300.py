import math
import sys
# ans 보다 같거나 작은 것의 갯수 k
N = int(input())
k = int(input())
start = 1
end = N**2
ans = 0
while start <= end:
    mid = (start + end) // 2
    ans = mid
    cnt = 0
    for i in range(1, int(mid**0.5) + 1):
        start_n = int(mid**0.5)
        end_n = N
        while start_n <= end_n:
            mid_n = (start_n + end_n) // 2
            if i*(mid_n+1) <= mid:
                start_n = mid_n + 1
            else:
                end_n = mid_n - 1
        cnt += (mid_n - i) * 2 + 1
    if cnt <= k:
        start = mid + 1
    else:
        end = mid - 1
print(ans)


