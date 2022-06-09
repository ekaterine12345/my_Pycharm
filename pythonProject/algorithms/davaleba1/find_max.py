a = [9, 205, 20, 40, 5]

mx = a[0]
for i in range(1, 5):
    if a[i] > mx:
        mx = a[i]
print(mx)
