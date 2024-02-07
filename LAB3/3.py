legs = int(input("How many legs: "))
heads = int(input("How many heads: "))
def solve(heads, legs):
    r_heads = int(legs / 2 - heads)
    c_heads = int(heads - r_heads)
    print(f"Chickens {c_heads}, and rabbits {r_heads}")
solve(heads, legs)
    



#solving
"""
4r + 2c = 94
2r + c = 47
r + c = 35
r = 12
c = 23
"""