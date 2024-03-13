def even(N):
    for i in range(0, N+1, 2):
        yield i

def pr():
    N = int(input("Number?\n"))
    even_numbers = even(N)
    print(*even_numbers, sep=', ')

if __name__ == "__main__":
    pr()
