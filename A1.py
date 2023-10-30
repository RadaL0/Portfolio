x = int(input())
y = int(input())
def paint (x):
    w = 0
    for i in range (x+1):
        if i*i > x:
            return int(x-w)
        w = i*i
if paint(x) + paint(y) < paint(x+y):
    print('Petya leaves paint to himself')
elif paint(x) + paint(y) == paint(x+y):
    print('Equal')
elif paint(x) + paint(y) > paint(x+y):
    print('Petya gives paint to Vasya')