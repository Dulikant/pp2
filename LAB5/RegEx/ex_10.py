import re

def a_b(s):
    x = re.sub(r'([a-z])([A-Z])', r'\1_\2',  s)
    return x.lower()


def main():
    s = input()
    y = a_b(s)
    print(y)

if __name__ == "__main__":
    main()
