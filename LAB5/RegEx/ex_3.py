import re

def a_b(s):
    x = re.split('_', s)
    return x

def main():
    s = input()
    y = a_b(s)
    print(*y, sep='')

if __name__ == "__main__":
    main()
