def volume(n):
    n = n ** 3
    other_cal = (4/3) * 3.14
    return n * other_cal

n = int(input("Radius?\n"))
print(volume(n))