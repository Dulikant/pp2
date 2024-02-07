def has_33(nums):
    j = len(nums)
    i = 0
    while i != j - 1:
        if nums[i] == nums[i + 1] == 3:
            return True
        else:
            i += 1
    return False
n = int(input())
nums = []
for i in range(n):
    m = int(input())
    nums.append(m)

print(has_33(nums))