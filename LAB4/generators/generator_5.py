def down(y):
    for i in range(0, y+1):
        yield i

def main():
    y = int(input("Number?\n"))
    num = down(y)
    print(*num[::-1])

if __name__ == "__main__":
    main()