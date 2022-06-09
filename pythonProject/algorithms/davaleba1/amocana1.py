a = 5
b = 16
c = 2

b = b//c*c
a1 = a
a = a//c*c

print(b//c - a//c + (a1 == a))
