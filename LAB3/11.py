name = input()
name_reversed = name[::-1]
if name_reversed == name:
    print("Palindrome")
else:
    print("Not palindrome")