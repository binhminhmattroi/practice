import sys
target = 13
print (f"target is {target}")
nums = [2,7,11,15]
print (nums)

num_map = {}
for i, num in enumerate(nums):
    print (f"elements are {i} , {num}")
    complement = target - num
    print (f"complement is  {complement}")
    complement = target - num
    if complement in num_map:
        print ("FOUND %s  %s" % (num_map[complement], i))
        exit(0)
    num_map[num] = i
    print (f"ANN the num_map is {num_map}")
