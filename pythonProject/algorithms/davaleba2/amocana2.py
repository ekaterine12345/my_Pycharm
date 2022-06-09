def to_sign_magnitude(n, b):
    ans2 = []

    if n >= 0:
        c = 0
    else:
        c = 1
        n = -n

    while n > 0:
        i = n % 2
        n //= 2
        ans2.append(i)

    l = b - 1 - len(ans2)
    while l > 0:
        ans2.append(0)
        l -= 1
    ans2.append(c)
    ans2.reverse()
    # for i in ans2:
    #     print(i, end="")
    # print()
    return ans2


def to_ones_complement(n, b):
    if n >= 0:
        return to_sign_magnitude(n, b)
    n = -n
    ans2 = to_sign_magnitude(n, b)
    for i in range(b):
        ans2[i] = 1 - ans2[i]

    return ans2


def to_twos_complement(n, b):
    if n >= 0:
        return to_sign_magnitude(n, b)
    ans = to_ones_complement(n, b)
    # for i in range(b-1, 0, -1):
    ans[b-1] += 1
    i = b-1
    while i > 0:
        if ans[i] >= 2:
            ans[i] = 0
            ans[i-1] += 1
        else:
            break
        i -= 1
    return ans


def pri(a):
    for i in a:
        print(i, end="")
    print()


# n = 123
# b = 8

# print(f"To signed magnitude base: ", end="")
# to_sign_magnitude(120, 8)
# to_sign_magnitude(-120, 8)
# print(f"To one's complement : ", end="")
# pri(to_ones_complement(120, 8))
# print(f"To one's complement : ", end="")
# pri(to_ones_complement(-120, 8))

print(f"To two's complement : ", end="")
pri(to_twos_complement(120, 8))
print(f"To two's complement : ", end="")
pri(to_twos_complement(-120, 8))
