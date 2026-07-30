import sys
target = 9
array = [2,7,11,15]
print (array)
for i in range(len(array)):
    for j in range(i+1, len(array)):
        total = array[i] + array[j]
        print(f"{array[i]} + {array[j]} = {total}")
        print(f"{i} , {j}")
        if (total == target):
            print ("DONE")
            sys.exit()
