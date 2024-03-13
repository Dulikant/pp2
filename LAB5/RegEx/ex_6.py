import re

def a_b(s):
    x = re.sub(r'[,. ]',r':', s)
    return x

def main():
    s = input()
    y = a_b(s)
    print(y)

if __name__ == "__main__":
    main()
