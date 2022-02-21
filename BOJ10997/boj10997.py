n = int(input())
if n-1:
    print('*'*(4*n-3))
    print('*')
    for i in range(1, n):
        print('* '*i, end='')
        print('*'*(4*n-4*i-1), end='')
        print(' *'*(i-1))
        print('* '*(i+1), end='')
        print(' '*(4*n-4*i-4), end='')
        print('* '*(i-1), end='*\n')
    print('* '*(2*n-2), end='*\n')
    for i in range(n-1, 0, -1):
        print('* '*i, end=' '*(4*n-4*i-3))
        print(' *'*i)
        print('* '*(i-1), end='*'*(4*n-4*i+1))
        print(' *'*(i-1))
else:
    print('*')