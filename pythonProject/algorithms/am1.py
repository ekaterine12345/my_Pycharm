a = [1, 2, 3, 100, 4, 5, 10, 30, 101, 101, 33]
x = 0
n = len(a)
mx = a[0]
j=0
ans = 0
for i in range(1, n):
    if a[i] > mx:
        mx = a[i]
        j = i
i=0
# print(j, mx)
while i <n:
    print(i, a[i], x)
    if a[i] == mx:
        x += 1
        print('x: ',x)
        ans = i
    if x == 2:
        print('ans', i)
    i += 1

