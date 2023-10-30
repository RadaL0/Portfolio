import sys
sys.setrecursionlimit(10000)
x = {}
def A(m, n):
    if not (m, n) in x:
        if m == 0:
            y = n + 1
        if m > 0 and n == 0:
            y = A(m - 1, 1)
        if m > 0 and n > 0:
            y = A(m - 1,A(m, n - 1))
        x[(m, n)] = y
    return x[(m, n)]
a, b = map(int,input().split())
print(A(a, b))