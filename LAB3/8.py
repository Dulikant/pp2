def spy_game(nums):
    list = []
    for i in nums:
        if i == 0 or i == 7:
            list.append(i)
        else:
            continue
    c = len(list)
    if list[0] == list[1] == 0 and list[2] == 7:
        return True
    else:
        return False
    

n = int(input())
nums = []
for i in range(n):
    m = int(input())
    nums.append(m)

print(spy_game(nums))