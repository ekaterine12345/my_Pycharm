def f(a, b, c):
    if a == b and a == c:
        return 3
    if a == b or a == c or b == c:
        return 2
    return 0


print(f(101, 105, 10))

# best case 2 comparsions
# worst case 4 comparision

