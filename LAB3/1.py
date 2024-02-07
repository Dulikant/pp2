def gramms_to_ounces(n):
    ounces = 28.3495231 * n
    return ounces

n = int(input("How many gramms?\n"))
print(gramms_to_ounces(n))