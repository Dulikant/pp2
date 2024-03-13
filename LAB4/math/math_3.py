import math

def area(n,l):
    s = n* (l ** 2) / (4 * math.tan(math.pi / n))
    return s

def main():
    n = int(input("Sides\n"))
    l = int(input("Length\n"))
    x = area(n,l)
    print(x)

if __name__ == "__main__":
    main()
