import re

def a_b(s):
    x = re.search(r'[A-Z][a-z]*',s)
    return x

def main():
    s = input()
    y = a_b(s)
    print(y)

if __name__ == "__main__":
    main()
