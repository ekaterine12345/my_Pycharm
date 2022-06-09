def from_sign_magnitude(n, b):
    a = [char for char in n]
    ans = 0

    for i in range (b-len(a)):
        a.insert(1, 0, )
    print(a)
    i = 0
    while b > 1:
        b -= 1
        if a[b] == '1':
            ans += pow(2, i)
        i += 1

    if a[0] == 1:
        b = -b

    return ans


a = "111111"
b = 8
print(from_sign_magnitude(a, b))

