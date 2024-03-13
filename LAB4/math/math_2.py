import math

def trapezoid(a, b, height):
    s = ((a+b)/2)*height
    return s
def main():
    a = int(input("First value\n"))
    b = int(input("Second value\n"))
    height = int(input("Height\n"))
    x = trapezoid(a, b, height)
    print(x)

if __name__ == "__main__":
    main()
    
