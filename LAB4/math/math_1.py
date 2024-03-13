import math

def degree(N):
    result = N * (math.pi / 180)
    return result
def main():
    N = int(input("Degree?\n"))
    n = degree(N)
    print(n)
    

if __name__ == "__main__":
    main()
