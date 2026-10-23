#input = [2,7,11,15]
#target = 9
'''
hash ={}
for i in input:
    print (input[i])
    diff = target-input[i]
    #traverse the hash table
    for key, value in hash:
        if diff in hash:
            print(int(i) and hash{diff})
            exit()
        else:
            # insert the element into the hash
            hash{i} = input[i]
'''

python
def two_sum(nums, target):
    seen = {}                      # value -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:           # O(1) lookup
            return [seen[diff], i]
        seen[num] = i              # store after checking
    return []                      # no pair found


