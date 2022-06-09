n = 5
a = [1, 2, 3, 4, 5]
max1 = a[0]
max2 = -10000
for i in range(1, n):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] > max2:
        max2 = a[i]
print(max2)
