n = int(input())
list = []
for i in range(n):
    m = int(input())
    if m in list:
        continue
    else:
        list.append(m)


for i in list:
    print(i, end=' ')