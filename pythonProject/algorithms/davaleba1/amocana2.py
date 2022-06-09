def to_number(c):
    k = ord(c)-48  # 0 is ascii
    if 0 <= k <= 9:
        return k
    return ord(c)-55  # ascii A 65 10-65


def to_char(t):
    if 0 <= t <= 9:
        return chr(t+48)
    return chr(t+55)


n = "AF90D"
p = 16
q = 2
# 12AC43
l = len(n)
ans = 0
i = 0
while l > 0:
    l -= 1
    ans += to_number(n[l]) * pow(p, i)
    i += 1

print("To decimal: ", ans)
ans2 = ""
while ans > 0:
    i = ans % q
    ans //= q
    ans2 = to_char(i) + ans2

print(f"To {q} base: ", ans2)
