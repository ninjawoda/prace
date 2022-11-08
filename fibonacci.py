x = 0
y = 1

z = int(input("do jakiej liczby ma się wykonywać ciag "))

while x < z:
    print(x)
    print(y)
    x, y = x+y, y+x+y