s = input()
li = [(int(s[x]) + int(s[x + 1])) / 2 for x in range(len(s) - 1)]

print(li)
