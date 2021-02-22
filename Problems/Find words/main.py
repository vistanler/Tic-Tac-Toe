a = input().split()
b = []
i = 0
for i in range(len(a)):
    if a[i].endswith('s'):
        b.append(a[i])
    i = i + 1

b = "_".join(b)
print(b)
