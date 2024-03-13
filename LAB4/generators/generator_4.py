def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def main():
    a = int(input("Start"))
    b = int(input("End"))
    x = squares(a, b)
    for i in x:
        print(i, sep=', ')

if __name__ == "__main__":
    main()