def squares(N):
    for i in range(1, N+1):
        yield i**2

N = int(input("Number?\n"))
n = squares(N)
for i in n:
    print(i)