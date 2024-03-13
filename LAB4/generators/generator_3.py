def div(N):
    for i in range(0, N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


def main():
    N = int(input("Number?\n"))
    divisible = div(N)
    for i in divisible:
        print(i, sep=', ')

if __name__ == "__main__":
    main()