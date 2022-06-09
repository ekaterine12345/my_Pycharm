file = open("capital.txt", "r")
ans = 0
for each in file:
    for c in each:
        if 'A' <= c <= 'Z':
            ans += 1
print(ans)
