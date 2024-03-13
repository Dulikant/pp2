import re

def a_b(s):
    x = re.search(r'a[b]*',s)
    return x

def main():
    s = input()
    y = a_b(s)
    print(y)

if __name__ == "__main__":
    main()
