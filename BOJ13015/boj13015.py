n = int(input())

print('*'*n, end=' '*(2*n-3))
print('*'*n)
for i in range(1, n-1):
    print(' '*i, end='*')
    print(' '*(n-2), end='*')
    print(' '*(2*n-2*i-3), end='*')
    print(' ' * (n - 2), end='*\n')
print(' '*(n-1), end='*')
print(' '*(n-2), end='*')
print(' '*(n-2), end='*\n')
for i in range(n-2, 0, -1):
    print(' '*i, end='*')
    print(' '*(n-2), end='*')
    print(' '*(2*n-2*i-3), end='*')
    print(' '*(n-2), end='*\n')
print('*'*n, end=' '*(2*n-3))
print('*'*n)