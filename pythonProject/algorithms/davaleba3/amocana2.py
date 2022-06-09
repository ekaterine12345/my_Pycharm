file = open("number.txt", "r")
sum = 0
n = 0
list = []
for each in file:
    list = each.split()
    for a in list:
        print(a)
        sum += int(a)
        n += 1
print(sum, n, sum/n)

