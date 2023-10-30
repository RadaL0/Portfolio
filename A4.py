def q(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * q(a, n - 1)
    elif n % 2 == 0:
        return q(a * a, n / 2)
a = float(input())
n = int(input())
c = q(a, n)
if c == int(c):
    c = int(c)
print(c)