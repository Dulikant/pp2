import math

def area(a,b):
    s = a * b
    return s

def main():
    a = int(input("Height\n"))
    b = int(input("Length\n"))
    x = area(a,b)
    print(x)

if __name__ == "__main__":
    main()